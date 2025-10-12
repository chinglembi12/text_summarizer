

from transformers import pipeline
#Using a resource cache is a key Streamlit optimization 
from streamlit import cache_resource

@cache_resource
def load_summarizer():
    #This function is responsible for loading the pre-trained summarization model
    return pipeline("summarization", model="facebook/bart-large-cnn")

# Generating
def generate_summary(text):
    summarizer = load_summarizer()
    summary = summarizer(
        text, 
        max_length=150,
        min_length=30, 
        do_sample=False
    )
    return summary[0]['summary_text']
