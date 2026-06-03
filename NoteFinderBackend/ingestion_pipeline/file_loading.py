'''
Makeo Tom
May 27, 2026
given a directory load all the notes files here
Description:
loads all files given a NOTES_LOCATION if they are a markdown
TODO support multiple file types
'''

from config import NoteFinderConfig as nfc

from langchain_community.document_loaders import TextLoader, DirectoryLoader
import os

def load_documents():
    '''
    (1) Load all of the documents and return them as langchain documents
    '''
    if not os.path.exists(nfc.NOTES_LOCATION):
        print(f'❌ directory {nfc.NOTES_LOCATION} does not exist and program will cease to work')
        return False
    

    print(f'⏳ loading directory ({nfc.NOTES_LOCATION})')
    loader = DirectoryLoader(
        path=nfc.NOTES_LOCATION,
        glob='*.md',
        loader_cls=TextLoader,
        recursive=True
    )
    documents = loader.load()
    print(f'✅ Loaded {len(documents)} documents\n')

    return documents