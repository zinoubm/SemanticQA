import pdfplumber
from pathlib import Path
import os

input_path = Path("./documents")

file_names = os.listdir(input_path)

result = ""

for file_name in file_names:
    pdf = pdfplumber.open(input_path / file_name)
    for page in pdf.pages:
        text = page.extract_text()
        result += text

# encoding to ASCII will remove special caracters.
result = result.encode(encoding="ASCII", errors="ignore").decode()

with open(input_path / "result.txt", "w") as f:
    f.write(result)
