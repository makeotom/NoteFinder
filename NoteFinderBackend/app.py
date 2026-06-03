'''
Makeo Tom
May 26, 2026
Backend Api (development)
'''

import ingestion_pipeline.ingestion as ingestion
import retrieval_pipeline.retrieval as retrieval

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {'status': 'good'}

@app.get('/retrieval/')
def read_retrieval_query(query:str, n:int):
    documents = retrieval.retrieval(query=query, n=n)
    return documents

@app.get('/ingestion/run')
def read_ingestion_run():
    ingestion.run()
    return {'status': 'good'}