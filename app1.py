import streamlit as st
from utils import extract_text_from_file, summarize_text, generate_tts

st.title("📄 DocSage AI - Smart SOP Summarizer")

uploaded_file = st.file_uploader("Upload a PDF or DOCX file", type=['pdf', 'docx'])

if uploaded_file:
    with st.spinner("Extracting text..."):
        raw_text = extract_text_from_file(uploaded_file)
        st.text_area("Extracted Text", raw_text[:2000], height=300)

    if st.button("Summarize"):
        with st.spinner("Generating summary..."):
            summary = summarize_text(raw_text)
            st.success("Summary Ready")
            st.text_area("Summary", summary, height=200)

            # Generate and play TTS
            path = generate_tts(summary)
            st.audio(path)

