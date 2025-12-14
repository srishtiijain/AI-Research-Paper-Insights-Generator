from transformers import pipeline
import os

input_folder = "outputs"
output_folder = "summaries"

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    if file.endswith(".txt"):
        with open(os.path.join(input_folder, file), "r", encoding="utf-8") as f:
            text = f.read()

        summary = summarizer(
            text,
            max_length=200,
            min_length=80,
            do_sample=False
        )[0]["summary_text"]

        out = file.replace(".txt", "_summary.txt")
        with open(os.path.join(output_folder, out), "w", encoding="utf-8") as f:
            f.write(summary)

print("summarization done")
