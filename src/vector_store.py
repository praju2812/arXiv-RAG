"""
ChromaDB-backed vector store for arXiv paper embeddings.
"""

from typing import Dict, List

import chromadb


class PaperVectorStore:
    """Persistent vector store wrapping ChromaDB for paper embeddings."""
    
    def __init__(
        self,
        collection_name: str = "arxiv_papers",
        persist_dir: str = "./chroma_db",
    ):
        """
        Initialise the vector store.
        
        Args:
            collection_name: Name of the ChromaDB collection.
            persist_dir: Local directory for ChromaDB persistence.
        """
        # create chromadb.PersistentClient pointing to persist_dir
        self.client = chromadb.PersistentClient(path=persist_dir)

        # get_or_create_collection with the given name
        self.collection = self.client.get_or_create_collection(name=collection_name)
        
    def add_papers(
        self,
        ids: List[str],
        embeddings: List[List[float]],
        documents: List[str],
        metadatas: List[Dict],
    ) -> None:
        """
        Add paper embeddings to the collection.
        
        Args:
            ids: Unique IDs for each paper.
            embeddings: Embedding vectors (each dim=768 for SPECTER).
            documents: The original text (typically abstracts) for each paper.
            metadatas: Dict of additional metadata per paper.
        """
        #Add the papers to the collection using self.collection.add()
        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas,
        )
    
    def query(
        self,
        query_embedding: List[float],
        top_k: int = 5,
    ) -> Dict:
        """
        Retrieve top-k papers most similar to the query embedding.
        
        Args:
            query_embedding: A single embedding vector to query with.
            top_k: Number of similar papers to return.
        
        Returns:
            Dict with keys 'ids', 'distances', 'documents', 'metadatas',
            each containing top-k results.
        """
        
        # Query the collection using self.collection.query() with the query_embedding and top_k
        # return the results in a dict
    
        raw = self.collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
    )
        # dict with keys 'ids', 'distances', 'documents', 'metadatas', each containing a list of lists (one per query). 
        # Since we have only one query, we take the first element of each list to return a dict of top-k results.
        return {
        "ids": raw["ids"][0],
        "distances": raw["distances"][0],
        "documents": raw["documents"][0],
        "metadatas": raw["metadatas"][0],
    }

    
    def count(self) -> int:
        """Return the number of papers in the collection."""
        return self.collection.count()


if __name__ == "__main__":
    import shutil
    
    # Smoke test — clean any prior test data
    test_dir = "./test_chroma"
    shutil.rmtree(test_dir, ignore_errors=True)
    
    store = PaperVectorStore(
        collection_name="test_collection",
        persist_dir=test_dir,
    )
    
    store.add_papers(
        ids=["test_001"],
        embeddings=[[0.1] * 768],
        documents=["This is a test abstract about machine learning."],
        metadatas=[{"title": "Test Paper", "categories": "cs.LG"}],
    )
    
    print(f"Collection has {store.count()} papers")
    
    results = store.query(query_embedding=[0.1] * 768, top_k=1)
    print(f"Query results:")
    for key, value in results.items():
        print(f"  {key}: {value}")
    
    # Clean up
    shutil.rmtree(test_dir, ignore_errors=True)
    print("\nTest passed and cleaned up.")