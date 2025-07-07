import streamlit as st
from utils import extract_text_from_file, summarize_text, generate_flowchart, generate_tts
from qa_bot import answer_question
import os

st.set_page_config(page_title="DocSage AI", layout="wide")
st.title("📄 DocSage AI – Smart SOP & Manual Analyzer")

uploaded_file = st.file_uploader("Upload a PDF or DOCX file", type=["pdf", "docx"])
query = st.text_input("Ask a question from the document (optional)", "")

if uploaded_file:
    text = extract_text_from_file(uploaded_file)
    st.subheader("📃 Extracted Text")
    st.text_area("Document Content", text[:3000], height=300)

    st.subheader("🧠 Summary")
    summary = summarize_text(text)
    st.success(summary)

    st.subheader("🔍 Answer a Question")
    if query:
        answer = answer_question(text, query)
        st.info(f"Answer: {answer}")

    st.subheader("🧭 Flowchart")
    flowchart_code = generate_flowchart(summary)
    st.graphviz_chart(flowchart_code)

    st.subheader("🔊 Text-to-Speech")
    tts_path = generate_tts(summary)
    if tts_path:
        st.audio(tts_path)