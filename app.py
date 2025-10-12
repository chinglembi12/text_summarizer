
import streamlit as st
#importing the function from the source folder
from src.model_loader import generate_summary

st.title("📄 AI Text Summarizer")
#

text_input = st.text_area("Paste your text here: ", height=300)

if st.button("Generate Summary"):
    if text_input:
        with st.spinner('Summarizing...'):
            
            summary_text = generate_summary(text_input)

        st.subheader("🔍 Summary")
        st.info(summary_text)
    else:
        st.warning("Please paste some text to summarize.")
