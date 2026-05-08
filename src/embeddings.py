"""
Embedding generation using SPECTER (allenai/specter).
SPECTER is a transformer model trained specifically for scientific text representations.
"""

from typing import List

from sentence_transformers import SentenceTransformer


class SpecterEmbedder:
    """Wraps SPECTER for batch embedding of scientific texts."""

    MODEL_NAME = "allenai/specter"
    
    def __init__(self):
        """Load the SPECTER model from HuggingFace."""
        self.model = SentenceTransformer(self.MODEL_NAME)
    
    def embed_texts(self, texts: List[str], batch_size: int = 32, show_progress_bar: bool = True) -> List[List[float]]:
        """
        Embed a list of texts in batches.
        
        Args:
            texts: List of strings to embed. For scientific papers, use 
                "{title} [SEP] {abstract}" format for best results.
            batch_size: Number of texts to encode per batch.
            show_progress_bar: Display tqdm progress bar during encoding.
        
        Returns:
            List of embedding vectors, each of dimension 768.
        """
        return self.model.encode(texts, batch_size=batch_size, show_progress_bar=show_progress_bar).tolist()
    
    def embed_query(self, query: str) -> List[float]:
        """
        Embed a single query string.
        
        Args:
            query: The query text to embed.
        
        Returns:
            Embedding vector as list of floats (dim=768).
        """
        return self.embed_texts([query], show_progress_bar=False)[0]      

if __name__ == "__main__":
    print("Loading SPECTER model...")
    embedder = SpecterEmbedder()
    
    print("\nEmbedding test query...")
    test = embedder.embed_query(
        "Attention Is All You Need [SEP] We propose a new architecture..."
    )
    print(f"Embedding dimension: {len(test)}")
    print(f"First 5 values: {test[:5]}")