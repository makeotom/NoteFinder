'''
Makeo Tom
May 26, 2026
Build a vector database based off notes
Description:
Run all core method of ingestion pipeline on a high level
'''

from ingestion_pipeline.chunking import elements_to_document, chunk_documents
from ingestion_pipeline.file_loading import load_documents
from ingestion_pipeline.vector_embedding import embed_documents

from config import NoteFinderConfig

def run():
    '''
    (0/1) basic functionality: load all .md files in the NOTES_LOCATION FOLDER
    (0/2) chunk all the documents
    (0/3) embed and save vector embeddings in database
    '''
    documents = load_documents()
    chunked_documents = chunk_documents(documents=documents)
    vector_store = embed_documents(chunked_documents=chunked_documents)