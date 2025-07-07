# 🧠 DocSage AI

DocSage AI is an AI-powered web app built with Streamlit that allows you to upload technical PDFs or Word documents (manuals, SOPs, guides) and get:

- Accurate AI-generated summaries
- Visual flowcharts of the procedures
- Text-to-speech audio
- Question-Answering (QA) from the document

## 🚀 How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

Make sure you set your OpenAI API Key as an environment variable:

```bash
export OPENAI_API_KEY=your_api_key_here
```

## 📁 Features
- PDF / DOCX parsing
- GPT-4 summarization + QA
- Graphviz flowcharts
- MP3 audio playback via gTTS

---

Built for engineers, techs, and field teams working with complex documentation like SOPs, controller manuals, and more.