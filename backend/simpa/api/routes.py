import asyncio
import typing as t
import redis.asyncio as redis

from fastapi import APIRouter
from simpa import config
from simpa.embeddings import Embeddings
from simpa.models import Paper

from simpa.schema import (
    PaperIdRequest,
    SimilarityRequest,
    UserTextSimilarityRequest
)
from simpa.search_index import SearchIndex

import requests
from bs4 import BeautifulSoup


paper_router = r = APIRouter()
redis_client = redis.from_url(config.REDIS_URL)
embeddings = Embeddings()
search_index = SearchIndex()

async def process_paper(p, i: int, paper_id) -> t.Dict[str, t.Any]:
    paper = await redis_client.hgetall(p.id)
    paper.pop(b"vector") 
    score = 1 - float(p.vector_score)
    paper['similarity_score'] = score
    return paper

async def papers_from_results(total, results) -> t.Dict[str, t.Any]:
    # extract papers from VSS results
    return {
        'total': total,
        'papers': [
            await process_paper(p, i)
            for i, p in enumerate(results.docs)
        ]
    }

# SIMPA
async def papers_from_results_simpa(results, paper_id) -> t.Dict[str, t.Any]:
    # extract papers from VSS results
    return {
        'papers': [
            await process_paper(p, i, paper_id)
            for i, p in enumerate(results.docs)
        ]
    }

@r.post("/vectorsearch/id", response_model=t.Dict)
async def find_papers_by_id(paperid_request: PaperIdRequest):
    print("Finding papers by paperid: ", paperid_request)
    # Create query
    query = search_index.vector_query(
        [],
        [],
        paperid_request.search_type,
        paperid_request.number_of_results
    )

    # find the vector of the Paper listed in the request
    paper_vector_key = "paper_vector:" + str(paperid_request.paper_id)
    vector = await redis_client.hget(paper_vector_key, "vector")

    # if the paper is not preprocessed yet in our db, infer vector on the fly 
    if not vector:
        vector = get_paper_title_desc_by_id(paperid_request.paper_id)

    # obtain results of the queries
    results = await redis_client.ft(config.INDEX_NAME).search(query, query_params={"vec_param": vector})
    
    # Get Paper records of those results
    return await papers_from_results_simpa(results, paperid_request.paper_id)

def get_paper_title_desc_by_id(paper_id):
    print("Getting paper title & desc on the fly for: ", paper_id)
    url = "https://arxiv.org/abs/{paper_id}".format(
        paper_id = paper_id
    )
    response = requests.get(url)
    soup = BeautifulSoup(response.text)

    metas = soup.find_all('meta')
    title_meta = [meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'citation_title']
    title = title_meta[0] if len(title_meta) > 0 else ""
    description_meta = [meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'citation_abstract']
    description = description_meta[0] if len(description_meta) > 0 else ""

    vector = embeddings.make(title + ' ' + description).tobytes()
    return vector