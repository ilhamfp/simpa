import os

PROJECT_NAME = "simpa"
API_DOCS = "/api/docs"
OPENAPI_DOCS = "/api/openapi.json"
API_V1_STR = "/api/v1"

INDEX_NAME="papers"
INDEX_TYPE = os.environ.get("VECSIM_INDEX_TYPE", "HNSW")
REDIS_HOST = os.environ.get("REDIS_HOST", "redis-12575.c22039.us-east-1-1.ec2.cloud.rlrcp.com")
REDIS_PORT = os.environ.get("REDIS_PORT", 12575)
REDIS_DB = os.environ.get("REDIS_DB", 0)
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", "pny1MVtrFoBOcDyvfFDBKQwHPkYWRVUN")
REDIS_URL = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"
os.environ["REDIS_DATA_URL"] = REDIS_URL
os.environ["REDIS_OM_URL"] = REDIS_URL
DATA_LOCATION = os.environ.get("DATA_LOCATION", "../../data")
