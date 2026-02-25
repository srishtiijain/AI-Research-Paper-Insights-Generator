import fitz
import os
import re
import sys
input_folder = "papers"
output_folder = "outputs"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(input_folder, filename)
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()

        output_name = filename.replace(".pdf", ".txt")
        output_path = os.path.join(output_folder, output_name)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)

print("done")
   
