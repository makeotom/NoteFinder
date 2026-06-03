'''
Makeo Tom
May 26, 2026
Given a query find documents
Description:
Have retrieval pipeline method at a high level to return relevant documents
'''

from langchain_postgres import PGVector
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import OllamaLLM
from config import NoteFinderConfig

import time
from json import loads

def retrieval(query, n=5):
    '''
    given query, return most relevant documents
    '''
    print(f'✅ Beginning retrieval process for query: ({query})')
    start = time.time()

    # create connection parameters for postgres
    connection = f'postgresql+psycopg://{NoteFinderConfig.DB_USER}:{NoteFinderConfig.DB_PASSWORD}@{NoteFinderConfig.DB_URL}:{NoteFinderConfig.DB_PORT}/{NoteFinderConfig.DB}'
    collection_name = NoteFinderConfig.DB_COLLECTION_NAME

    # create embedding model
    embedding_model = OllamaEmbeddings(model=NoteFinderConfig.EMBEDDING_MODEL)

    # fetch existing vector database
    conn = PGVector(
        connection=connection,
        collection_name=collection_name,
        embeddings=embedding_model,
        use_jsonb=True,
        collection_metadata={
            'hnsw:space':'cosine'
        }
    )

    retriever = conn.as_retriever(
        search_kwargs={
            'k': f'{n}'
        }
    )

    
    # with many different queries retrieve many relevant documents
    document_grid = []
    queries = generate_queries(query=query)
    for i, q in enumerate(queries):
        print(f'({i + 1}/{len(queries)}) matching query to similar documents', end='')
        docs = similar_documents(query=q, retriever=retriever)
        print('\t✅ DONE ✅')
        document_grid.append(docs)
    
    print('🕓 finalizing correct documents')
    final_documents = select_documents(query=queries, document_grid=document_grid)

    elapsed = time.time() - start
    print(f'🎉 Created in {elapsed} seconds\n')

    return [format_document(document) for document in final_documents]


def generate_queries(query, k=1):
    '''
    given one query generate similar queries 
    '''

    return [query]

def similar_documents(query, retriever):
    '''
    given one query return n documents that are similar
    '''
    documents = retriever.invoke(query)
    return documents


def select_documents(query, document_grid):
    '''
    given all document lists return the most relevant ones
    this is two step retrieval
    '''
    if document_grid:
        return document_grid[0]

def format_document(document):
    '''
    given a list of documents, format in them in the folowing format:
    document
    |---filename:str
    |---file_directory:str
    |---location:str
    |---page_content:str
    '''
    class FormattedDocument:
        filename = ''
        file_directory = ''
        location = ''
        page_content = ''

    formatted = FormattedDocument()
    metadata = loads(document.metadata['note-finder-data'])
    formatted.filename = metadata['filename']
    formatted.file_directory = metadata['file_directory']
    formatted.location = metadata['location']
    formatted.page_content = document.page_content

    return formatted