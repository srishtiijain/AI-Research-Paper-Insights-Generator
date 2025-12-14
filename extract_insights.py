import os
import re

input_folder = "outputs"
output_folder = "insights"

os.makedirs(output_folder, exist_ok=True)

sections = {
    "abstract": r"abstract([\s\S]*?)(introduction|methodology|methods)",
    "introduction": r"introduction([\s\S]*?)(methodology|methods|results)",
    "methodology": r"(methodology|methods)([\s\S]*?)(results|experiments)",
    "results": r"(results|experiments)([\s\S]*?)(conclusion|discussion)",
    "conclusion": r"(conclusion|discussion|future work)([\s\S]*)"
}

for file in os.listdir(input_folder):
    if file.endswith(".txt"):
        with open(os.path.join(input_folder, file), "r", encoding="utf-8") as f:
            text = f.read().lower()

        insights = ""

        for name, pattern in sections.items():
            match = re.search(pattern, text)
            if match:
                insights += f"\n{name.upper()}\n"
                insights += match.group(1).strip()[:1500]
                insights += "\n"

        out_file = file.replace(".txt", "_insights.txt")
        with open(os.path.join(output_folder, out_file), "w", encoding="utf-8") as f:
            f.write(insights)

print("insights extracted")
