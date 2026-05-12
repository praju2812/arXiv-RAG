"""
Load HF_TOKEN from .env
Accept a query (string) and context (list of retrieved abstracts)
Format them into a prompt — something like "Answer this question using the provided research papers: {query}\n\nContext: {context}"
Send that prompt to Groq using chat completions and model: llama-3.1-8b-instant
Return the generated answer as a string
"""

from typing import List

from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()

class Generator:

    """
    Generates answer based on query and context
    """
    MODEL_NAME = "llama-3.1-8b-instant"
    def __init__(self):
        
        self.model= self.MODEL_NAME
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))


    def generate_answers(self,query:str, context:List[str])-> str:

        """
        Generates answer on the basis of query and context
        """

        context = "\n\n".join(context)
        prompt = (
        f"Answer the following question using ONLY the provided research paper abstracts. "
        f"Do not use any outside knowledge. If the answer cannot be found in the abstracts, say so.\n\n"
        f"Question: {query}\n\n"
        f"Abstracts:\n{context}"
)
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=512
        )

        return response.choices[0].message.content
    

if __name__ == "__main__":
    print (" Generator starting..")
    query="Machine Learning papers"
    context = ["Machine Learning papers is a very diverse topic."]
    generator = Generator()
    answer= generator.generate_answers(query=query, context=context)
    print(answer)
