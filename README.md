<p align="center"> <img src="assets/logo_with_title.png" alt="simpa_logo" width="250"/>

## What?
Similar paper chrome extension for paperswithcode.com

Chrome extension code: [github.com/christianwbsn/simpa-ext](https://github.com/christianwbsn/simpa-ext)

## Why?
As academia and researcher, have you ever browse [paperswithcode.com](https://paperswithcode.com/) and thought:

> Hmm, this paper is interesting... I wonder are there any similar paper to this?

Because we did, and that's why we built Simpa: a similar paper chrome extension for paperswithcode!

With Simpa you can find out papers that are similar to the paper you're currently browsing as easy as one click! Simpa will also automatically **compare** and **contrast** paper by utilizing the 5Ws + 1H (What, Why, When, Where, Who, and How). So you can also easily read what makes them similar & different.

> Meaningful comparison, however, can enlighten an audience toward unknown similarities or differences between subjects. The more informative or surprising a comparative is, the more likely an audience is to be engaged.


<p align="center"> <img src="assets/demo.gif" alt="simpa_demo"/>

## Installation Guide
Follow the installation guide [here](https://github.com/christianwbsn/simpa-ext)

## Who?
Who's going to benefit?
* Academia who need more resources and inspirations for their thesis
* ML Practitioners who want to implement new method or even go back to older method
* Researchers who want to do comparison and contrast writing
* Avid paperswithcode fans

## Where?
For now Simpa works smoothly in [paperswithcode.com](https://paperswithcode.com/). This extension serves as a tribute to the community, because as ML practitioners, paperswithcode is one of the websites that greatly contributes to the advancement of machine learning research

## How
We build Simpa using Redis Cloud Vector Database, Saturn Cloud, and Huggingface. There are 4 main component to this project:
* Text Embedding & Paper Processing
* Redis Cloud & RediSearch Vector Similarity Search
* Saturn Cloud & FastAPI Deployment
* Google Chrome Extension

Here's an overview of the app:

<p align="center"> <img src="assets/Simpa_App_Diagram.png" alt="simpa_overview" width="750"/>

### API Docs
Open API Documentation for our webserver can be accessed here:
[https://simpa.community.saturnenterprise.io/api/docs](https://simpa.community.saturnenterprise.io/api/docs)

<p align="center"> <img src="assets/be.png" alt="simpa_overview" width="750"/>

More details on the backend [here](/backend/simpa/)

## Authors
* [Christian Wibisono](https://github.com/christianwbsn)
* [Ilham Firdausi Putra](https://github.com/ilhamfp)