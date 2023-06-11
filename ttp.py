from flask import Flask, request
import subprocess

app = Flask(__name__)

LANGUAGE_CODES = {
    "English": "en",
    "Spanish": "es",
    "Italian": "it",
    "German": "de",
    "French": "fr",
    "Portuguese": "pt"
}

def text_to_phonemes(text, language):
    espeak_language_code = LANGUAGE_CODES.get(language, "en")  # default to English if no match found
    return subprocess.check_output(["espeak", "-v", espeak_language_code, "-q", "--ipa", text]).decode('utf-8').strip()

@app.route('/text_to_phonemes', methods=['POST'])
def handle_text_to_phonemes():
    text = request.json['text']
    language = request.json['language']
    phonemes = text_to_phonemes(text, language)
    return {'phonemes': phonemes}

