import os

# Set ffmpeg path manually
os.environ["PATH"] += os.pathsep + r"C:\Users\Pc\Downloads\ffmpeg-7.1.1-essentials_build\ffmpeg-7.1.1-essentials_build\bin"

import whisper
import os
import language_tool_python
import pandas as pd

# Load Whisper model
model = whisper.load_model("base")

# Load grammar checker
tool = language_tool_python.LanguageTool('en-US')

def transcribe_and_score(folder_path):
    results = []

    for file in os.listdir(folder_path):
        if file.endswith(".wav") or file.endswith(".mp3"):
            file_path = os.path.join(folder_path, file)
            print(f"Processing {file_path}...")

            # Transcribe using Whisper
            result = model.transcribe(file_path)
            transcript = result["text"]

            # Score grammar
            matches = tool.check(transcript)
            errors = len(matches)
            words = len(transcript.split())
            score = max(0, 100 - (errors / words * 100)) if words > 0 else 0

            results.append({
                "filename": file,
                "transcript": transcript,
                "grammar_score": round(score, 2),
                "errors": errors,
                "issues": [m.message for m in matches]
            })

    return pd.DataFrame(results)

# Run
audio_folder = "grammar_audio_dataset"
df = transcribe_and_score(audio_folder)
df.to_csv("grammar_score_results.csv", index=False)
print("Done! Results saved to grammar_score_results.csv")



