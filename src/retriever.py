"""
It takes a query string as input
It uses SpecterEmbedder.embed_query() to turn that string into a vector
It passes that vector to PaperVectorStore.query() to get raw results
It zips the raw results (ids, distances, documents, metadatas) into a clean list of dicts that the rest of the app can use
"""
from typing import List, Dict
from src.embeddings import SpecterEmbedder
from src.vector_store import PaperVectorStore

class Retriever:
    """
    Retrieves relevant papers based on query

    Args:
        query (str): The query string to search for relevant papers

    Returns:
        List[Dict]: A list of dictionaries containing the retrieved papers' information
    """

    def __init__(self, collection_name: str = "arxiv_papers", persist_dir: str = "./chroma_db"):
        self.embedder = SpecterEmbedder()
        self.vector_store = PaperVectorStore(collection_name=collection_name, persist_dir=persist_dir) 

    def retrieve(self, query: str) -> List[Dict]:
        """
        Retrieves relevant papers based on query

        Args:
            query (str): The query string to search for relevant papers

        Returns:
            List[Dict]: A list of dictionaries containing the retrieved papers' information
        """
        query_vector = self.embedder.embed_query(query)
        raw_results= self.vector_store.query(query_vector)

        # Zip the raw results into a clean list of dicts
        results = []
        for id, distance, document, metadata in zip(
            raw_results["ids"],
            raw_results["distances"],
            raw_results["documents"],
            raw_results["metadatas"],
        ):
            results.append({
                "id": id,
                "distance": distance,
                "abstract": document,
                "authors": metadata.get("authors", ""),
                "title": metadata.get("title", ""),
                "categories": metadata.get("categories", ""),
            })

        return results
    
if __name__ == "__main__":
    retriever = Retriever()
    query = "What are the latest advancements in machine learning?"
    results = retriever.retrieve(query)
    print(results)
        
    
