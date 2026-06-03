'''
Makeo Tom
May 27, 2026
Given documents, partition and chunk all documents
Description:
Right now document partitioning only works with markdown files and no images or table or other content
TODO implement pdf parsing
TODO implement handwritten note parsing
possibly TODO -> implement a method to classify note taker types so handwritten notes can be parsed better
                -> might require user research on handwritten notes
'''

from unstructured.partition.md import partition_md
from unstructured.chunking.title import chunk_by_title

from langchain_core.documents import Document
import json

def chunk_documents(documents):
    '''
    (2) chunk all the documents are return them as a list of langchain documents
    '''
    print('Chunking phase beginning\n--------------------')

    # (1) -> partition documents by title in markdown text
    print(f'🕓 partitioning {len(documents)} mark down files...')

    partitioned_documents = []
    for i, document in enumerate(documents):
        filename = document.metadata['source']
        partitioned_document = partition_md(
            filename=filename
        )
        partitioned_documents.append(partitioned_document)

        print(f'✅ {i + 1}/{len(documents)} documents partitioned')
    
    # (2) -> chunk the partitioned documents
    print('\n🕓 chunking partitioned documents...')

    chunked_documents = []
    for i, elements in enumerate(partitioned_documents):
        chunked_document = chunk_by_title(
            elements=elements,
            max_characters=3000,
            new_after_n_chars=2400,
            combine_text_under_n_chars=100
        )
        chunked_documents.append(chunked_document)

        print(f'✅ {i + 1}/{len(documents)} documents chunked')

    print('\n🎉 Chunking phase finished\n')

    clist = [elements_to_document(elements) for elements in chunked_documents]
    chunks = []
    for document in clist:
        for chunk in document:
            chunks.append(chunk)
    
    return chunks

def elements_to_document(elements):
    '''
    take a list of elements and convert the type to a list of document
    '''

    documents = []
    for i, element in enumerate(elements):
        # find a location indicator if any (a location indicator is some title or page number that identifies
        # where in a document the chunk references)
        location_indicator = ''
        if element.metadata.orig_elements:
            location_indicator = element.metadata.orig_elements[0].text
        document = Document(
            page_content=element.text,
            metadata={
                'note-finder-data': json.dumps({
                    'filename': element.metadata.filename,
                    'file_directory': element.metadata.file_directory,
                    'filetype': element.metadata.filetype,
                    'location': location_indicator
                })
            }
        )
        documents.append(document)

    return documents