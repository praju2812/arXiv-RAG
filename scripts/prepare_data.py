"""
Filter arXiv metadata to a focused subset for the RAG demo.

Streams the full ~4GB arXiv JSON Lines file and produces ~5K papers
in CS/ML categories.

Usage:
    python scripts/prepare_data.py
"""

import json
from pathlib import Path

# === Config ===
INPUT_PATH = Path("data/arxiv-metadata-oai-snapshot.json")
OUTPUT_PATH = Path("data/arxiv_cs_ml_subset.jsonl")
TARGET_CATEGORIES = {"cs.LG", "cs.AI", "cs.CL", "cs.CV", "stat.ML"}
MAX_PAPERS = 5000


def filter_arxiv():
    """Stream-filter arXiv JSON Lines file to target categories."""
    if not INPUT_PATH.exists():
        raise FileNotFoundError(
            f"Input file not found at {INPUT_PATH}. "
            f"Download from https://www.kaggle.com/datasets/Cornell-University/arxiv "
            f"and place in data/ directory."
        )
<<<<<<< HEAD
    
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    
    count = 0
=======
    # Make sure output directory exists
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    
    count = 0
    # Stream through input file line by line to avoid memory issues, filter by category, and write out matching papers
>>>>>>> c4448dab2a3faa09e5517e8168fc35356eb67a89
    with open(INPUT_PATH, "r") as fin, open(OUTPUT_PATH, "w") as fout:
        for line in fin:
            paper = json.loads(line)
            paper_cats = set(paper.get("categories", "").split())
            
            if paper_cats & TARGET_CATEGORIES:
                filtered = {
                    "id": paper["id"],
                    "title": paper["title"].strip(),
                    "abstract": paper["abstract"].strip(),
                    "authors": paper.get("authors", ""),
                    "categories": paper["categories"],
                    "update_date": paper.get("update_date", ""),
                }
                fout.write(json.dumps(filtered) + "\n")
                count += 1
                
                if count >= MAX_PAPERS:
                    break
                
                if count % 500 == 0:
                    print(f"Processed {count} papers...")
    
    print(f"\nDone. Saved {count} papers to {OUTPUT_PATH}")


if __name__ == "__main__":
    filter_arxiv()