# NoteFinder

#### Description

All encompassing ecosystem for notes.

## TODO

(done) reafactor retrieval pipeline to use the static data class,
(done) use base_url to access my stronger computer for the ollama llm url and embedding url
develop a bare minimum to query for documents mvp
choose cloud azure or aws (do aws please for resume value)

## Arcitecture

### Tech Stack

Back-end: Fast api
Front-end: react
UI-ux: tailwind
Core Rag: Lang Chain - Unstructured
Handwritten Note Chunker: OpenCV - findCotour
VectorDB; PostgressPG vector

### Core elements

Backend: web server, core functionality to contain retrieval and embedding pipeline
├── port: 8828
├── url: localhost
Vector DB: postgressql pg -> docker
├── port: 5431
├── url: localhost
Frontend: react, tailwind, some nice ui library
├── port: 80
LLM: Ollama - Gemma4
├── url: localhost -> (later my own home server for personal usage)
├── port: 11434


## MVP
Description: Given a folder location with .txt documents, if a question is asked return the most relevant documents. There should be a basic ui and postgresql db