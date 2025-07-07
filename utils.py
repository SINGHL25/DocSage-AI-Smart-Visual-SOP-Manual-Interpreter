import os
import tempfile
import docx2txt
import fitz  # PyMuPDF
import openai
from gtts import gTTS

def extract_text_from_file(uploaded_file):
    _, ext = os.path.splitext(uploaded_file.name)
    if ext.lower() == '.pdf':
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        return " ".join([page.get_text() for page in doc])
    elif ext.lower() == '.docx':
        temp_path = tempfile.NamedTemporaryFile(delete=False, suffix=".docx").name
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.read())
        return docx2txt.process(temp_path)
    return ""

def summarize_text(text):
    import openai
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Summarize the following technical document:
{text[:4000]}"}],
        temperature=0.5
    )
    return response.choices[0].message.content.strip()

def generate_flowchart(summary):
    steps = [line for line in summary.split('.') if line.strip()]
    flowchart = "digraph G {
"
    for i, step in enumerate(steps[:-1]):
        flowchart += f'  "{step.strip()}" -> "{steps[i+1].strip()}";
'
    flowchart += "}"
    return flowchart

def generate_tts(text):
    path = "/mnt/data/summary.mp3"
    tts = gTTS(text[:500], lang="en")
    tts.save(path)
    return path