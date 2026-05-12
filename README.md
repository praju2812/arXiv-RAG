---
title: arXiv RAG
emoji: 📚
colorFrom: blue
colorTo: green
sdk: streamlit
sdk_version: 1.35.0
app_file: app/streamlit_app.py
pinned: false
---

# arXiv-RAG

A Retrieval-Augmented Generation system over arXiv CS/ML paper abstracts. 
Ask natural-language questions and get answers grounded in relevant academic 
papers with citations.

## Why this exists
RAG systems are increasingly important for grounding LLM outputs in factual 
sources. This project demonstrates an end-to-end RAG pipeline built over 
~5,000 arXiv papers in computer science and machine learning categories.

## Data

This project uses the [arXiv metadata dataset](https://www.kaggle.com/datasets/Cornell-University/arxiv) from Kaggle, filtered to a focused subset for tractable demos:

- **Source:** ~2.5M arXiv papers (full dataset)
- **Filter:** Papers in CS/ML categories — `cs.LG`, `cs.AI`, `cs.CL`, `cs.CV`, `stat.ML`
- **Subset size:** 5,000 papers (most recent first)
- **Fields used:** `id`, `title`, `abstract`, `authors`, `categories`, `update_date`

The full dataset (~4GB) is processed via streaming to produce a ~7MB filtered file. See `scripts/prepare_data.py` for the pipeline.

To reproduce:
1. Download `arxiv-metadata-oai-snapshot.json` from Kaggle
2. Place in `data/`
3. Run `python scripts/prepare_data.py`

## Stack
- **Embeddings:** SPECTER (allenai/specter) — purpose-built for scientific text
- **Vector store:** ChromaDB (local persistent)
- **Generation:** Llama 3.1 (via Groq API)
- **UI:** Streamlit

## Architecture
Query → SPECTER embeddings → ChromaDB similarity search → top-5 abstracts → Llama 3.1 (Groq) → grounded answer

## Demo
[Live Demo](https://huggingface.co/spaces/Prajakta2812/arxiv-rag)

## Status
Deployed

## Setup
[to be added]

## License
MIT
