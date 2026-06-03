'''
Makeo Tom
May 27, 2026
Create vector embeddings
Description:
Right now, document are given and embeded with the .page_content and meta data is saved,
But everytime embed_documents is called, it removes the previous database values,
TODO implement a method that replaces only vector entries that have changed -> in other words only add embeddings for changed or updated notes
    last_modified is metadata that is kept track of
'''

from config import NoteFinderConfig as nfc

from langchain_ollama import OllamaEmbeddings
from langchain_postgres import PGVector

import time
import psycopg

def clear_previous_embeddings(collection_name, connection):
    '''
    remove all previous embeddings from the database
    '''

    # Source - https://stackoverflow.com/a/75534808
    # Posted by bigkeefer
    # Retrieved 2026-05-27, License - CC BY-SA 4.0
    print(f'attempting the following connection ({collection_name}):\n\t{connection}')
    with psycopg.connect(f'postgresql://{nfc.DB_USER}:{nfc.DB_PASSWORD}@{nfc.DB_URL}:{nfc.DB_PORT}/{nfc.DB}') as conn:
        print('✅ connection successfull!')
        cursor = conn.cursor()
        cursor.execute(f'DELETE FROM langchain_pg_embedding WHERE collection_id = (SELECT uuid FROM langchain_pg_collection WHERE name = %s)',
                       (collection_name,))
        return True

    print('❌ failed connection...')
    return False


def embed_documents(chunked_documents):
    '''
    embed documents to postgres vector database
    '''
    print('⏳Creating vector store and embedding chunks')
    print('--------------------\n')
    start = time.time()

    # create embedding model
    embedding_model = OllamaEmbeddings(model=nfc.EMBEDDING_MODEL, base_url=f'{nfc.EMBEDDING_MODEL_URL}:{nfc.EMBEDDING_MODEL_PORT}')

    # create connection parameters for postgres
    connection = f'postgresql+psycopg://{nfc.DB_USER}:{nfc.DB_PASSWORD}@{nfc.DB_URL}:{nfc.DB_PORT}/{nfc.DB}'
    collection_name = nfc.DB_COLLECTION_NAME

    # delete previous embeddings
    clear_previous_embeddings(connection=connection, collection_name=collection_name)

    print(f'⏳embedding {len(chunked_documents)} chunks...')

    # make the actual embeddings
    vector_store = PGVector.from_documents(
        documents=chunked_documents,
        embedding=embedding_model,
        connection=connection,
        collection_name=collection_name,
        use_jsonb=True,
        collection_metadata={
            'hnsw:space':'cosine'
        }
    )
    print('✅ documents embedded')
    elapsed = round(time.time() - start, 2)
    print(f'🎉 Created in {elapsed} seconds\n')

    return vector_store