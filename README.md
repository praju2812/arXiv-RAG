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

The full dataset (~4GB) is processed via streaming to produce a ~5MB filtered file. See `scripts/prepare_data.py` for the pipeline.

To reproduce:
1. Download `arxiv-metadata-oai-snapshot.json` from Kaggle
2. Place in `data/`
3. Run `python scripts/prepare_data.py`

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
