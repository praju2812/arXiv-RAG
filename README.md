# arXiv-RAG

A Retrieval-Augmented Generation system over arXiv CS/ML paper abstracts. 
Ask natural-language questions and get answers grounded in relevant academic 
papers with citations.

## Why this exists
RAG systems are increasingly important for grounding LLM outputs in factual 
sources. This project demonstrates an end-to-end RAG pipeline built over 
~5,000 arXiv papers in computer science and machine learning categories.

## Stack
- **Embeddings:** SPECTER (allenai/specter) — purpose-built for scientific text
- **Vector store:** ChromaDB (local persistent)
- **Generation:** HuggingFace Inference API
- **UI:** Streamlit

## Architecture
[diagram or text architecture description]

## Demo
[link to HuggingFace Spaces deployment — to be added]

## Status
🚧 In active development

## Setup
[to be added]

## License
MIT
