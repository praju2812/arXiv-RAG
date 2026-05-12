"""
Load the 5K filtered papers from prepare_data.py output
Instantiate SpecterEmbedder
Instantiate PaperVectorStore
Loop through papers, embed them, add to the store
Persist the ChromaDB index to disk
"""
import json

from src.embeddings import SpecterEmbedder
from src.vector_store import PaperVectorStore

def build_index():
    """ 
    Build the ChromaDB index from the filtered arXiv papers.
    
    Args:
        None

    Returns:
        None
    """

    # Load filtered papers from data/arxiv_cs_ml_subset.jsonl
    papers=[]
    with open("data/arxiv_cs_ml_subset.jsonl", "r") as fin:
        for line in fin:
            papers.append(json.loads(line))
    print(f"Loaded {len(papers)} papers from filtered dataset.")

    # Instantiate the SpecterEmbedder and PaperVectorStore
    embedder = SpecterEmbedder()
    vector_store = PaperVectorStore()

    embeddings = []
    ids = []
    documents = []
    metadatas = []

    # Embed the text and store the results
    texts = [f"{p['title']} [SEP] {p['abstract']}" for p in papers]
    embeddings = embedder.embed_texts(texts, batch_size=32)

    # Prepare the data for adding to the vector store
    for paper in papers:
        paper_id = paper["id"]
        title = paper["title"]
        abstract = paper["abstract"]
        authors = paper.get("authors", "")
        categories = paper["categories"]
        update_date = paper.get("update_date", "")
        metadata = {
            "id": paper_id,
            "title": title,
            "abstract": abstract,
            "authors": authors,
            "categories": categories,
            "update_date": update_date,
        }
        ids.append(paper_id)
        documents.append(abstract)
        metadatas.append(metadata)

    # Add the papers to the vector store
    vector_store.add_papers(ids=ids, embeddings=embeddings, documents=documents, metadatas=metadatas)
    print(f"Added {len(papers)} papers to the vector store.")

if __name__ == "__main__":
    build_index()