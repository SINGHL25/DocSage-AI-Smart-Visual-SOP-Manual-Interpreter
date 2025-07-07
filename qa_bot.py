import openai
import os

def answer_question(document_text, question):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers questions from manuals."},
            {"role": "user", "content": f"Document:
{document_text[:4000]}

Question: {question}"}
        ],
        temperature=0.4
    )
    return response.choices[0].message.content.strip()