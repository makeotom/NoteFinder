'''
Makeo Tom
May 27
environemt varible config class
'''

import os
from dotenv import load_dotenv

# load global enviornment varibles
load_dotenv()
class NoteFinderConfig:
    DB_URL:str = os.environ['DB_URL']
    DB_PORT:int = os.environ['DB_PORT']
    DB_USER:str = os.environ['DB_USER']
    DB_PASSWORD:str = os.environ['DB_PASSWORD']
    DB:str = os.environ['DB']
    DB_COLLECTION_NAME:str = os.environ['DB_COLLECTION_NAME']

    LLM_URL:str = os.environ['LLM_URL']
    LLM_PORT:int = os.environ['LLM_PORT']

    EMBEDDING_MODEL:str = os.environ['EMBEDDING_MODEL']
    EMBEDDING_MODEL_URL:str = os.environ['EMBEDDING_MODEL_URL']
    EMBEDDING_MODEL_PORT:int = os.environ['EMBEDDING_MODEL_PORT']

    NOTES_LOCATION:str = os.environ['NOTES_LOCATION']