"""
Import Pipeline, cache and load it
Title and brief description
Text input for query
Button to trigger search
Spinner while pipeline runs
Try/except around pipeline.run() — show st.error() on exception
Display answer prominently
Loop through papers and display title, authors, abstract
"""

import os
import sys

# step 1: get absolute path of this file
current_file = os.path.abspath(__file__)

# step 2: get app/ directory
app_dir = os.path.dirname(current_file)  

# step 3: get project root (one more level up)
project_root = os.path.dirname(app_dir)

# step 4: insert into sys.path
sys.path.insert(0, project_root)

import streamlit as st
from src.pipeline import Pipeline

@st.cache_resource(show_spinner=False)
def load_pipeline():
    """Load the main pipeline with caching to speed up subsequent runs."""
    return Pipeline()   

def main():
    
    with st.spinner("Loading pipeline..."):
        pipeline = load_pipeline()

    st.title("arXiv RAG Demo")
    st.write("Ask a question about machine learning research and get an answer with relevant papers!")

    query = st.text_input("Enter your query here:")
    if st.button("Search"):
        if not query.strip():
            st.error("Please enter a valid query.")
            return
        
        
        with st.spinner("Running the pipeline..."):
            try:
                result = pipeline.run(query)
                st.subheader("Generated Answer:")
                st.write(result["answer"])
                
                st.subheader("Retrieved Papers:")
                for paper in result["papers"]:
                    st.markdown(f"**{paper['title']}** by {paper['authors']}")
                    st.write(paper["abstract"])
            except Exception as e:
                st.error(f"An error occurred: {e}")

main()