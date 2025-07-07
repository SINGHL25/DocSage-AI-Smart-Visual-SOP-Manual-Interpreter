from gtts import gTTS
import os

def generate_tts(text, output_path="output.mp3"):
    try:
        tts = gTTS(text)
        tts.save(output_path)
        return output_path
    except Exception as e:
        return f"Error generating TTS: {e}"
