"""
Validate query isn't empty
Retrieve papers using Retriever
Extract abstracts from results
Generate answer using Generator
Return answer + papers
"""

from src.retriever import Retriever
from src.generator import Generator 

class Pipeline:
    """
    Main pipeline function to process the query and return answer + papers

    Args:
        query (str): The input query string

    Returns:
        dict: A dictionary containing the generated answer and retrieved papers
    """

    def __init__(self):
        self.retriever = Retriever()
        self.generator = Generator()

    def run ( self, query: str) -> dict:
        if not query.strip():
            raise ValueError("Query cannot be empty.")
        
        retrieved_papers = self.retriever.retrieve(query)
        abstracts = [paper["abstract"] for paper in retrieved_papers]

        if abstracts:
            try:
                answer = self.generator.generate_answers(query=query, context=abstracts)
            except Exception as e:
                raise RuntimeError(f"Error generating answer: {e}")
        else:
            raise ValueError("No relevant papers found.")

        return {
            "answer": answer,
            "papers": retrieved_papers
        }

if __name__ == "__main__":
    pipeline = Pipeline()
    query = "What are the latest advancements in machine learning?"
    result = pipeline.run(query)
    print("Generated Answer:")
    print(result["answer"])
    print("\nRetrieved Papers:")
    for paper in result["papers"]:
        print(f"- {paper['title']} by {paper['authors']} (ID: {paper['id']})")