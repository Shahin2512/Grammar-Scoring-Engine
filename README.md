# Grammar-Scoring-Engine
This project automatically transcribes audio files using OpenAI's Whisper and evaluates the grammar of the resulting text using LanguageTool. It helps in assessing the grammatical accuracy of spoken English through audio inputs.

🚀 Features
🎙️ Audio Transcription using Whisper (base model)

✅ Grammar Checking using LanguageTool (en-US)

📊 Scoring System: Calculates a grammar score based on detected grammatical issues

📁 Batch Processing of .wav and .mp3 files from a folder

🧾 CSV Export of all results (transcript, score, errors)

🧠 How It Works
Transcribes each audio file to text using Whisper

Checks grammar using LanguageTool

Calculates a grammar score using the formula:
Grammar Score = 100 - (Grammar Errors / Word Count) * 100

