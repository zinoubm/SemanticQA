import os
import re
from pathlib import Path
from dotenv import load_dotenv

import openai
import textwrap
import jsonlines

from src.utils import gpt3_embeddings

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

path = Path("./documents")


with open(path / "result.txt", "r") as f:
    lines = f.readlines()
    text = "".join(lines)
    text = re.sub("\s+", " ", text)  # white space normalization

result = []

chunks = textwrap.wrap(text, 4000)
for chunk in chunks:
    embedding = gpt3_embeddings(chunk)
    info = {"content": chunk, "embedding": embedding}
    result.append(info)

result_path = Path("./index")

with jsonlines.open(result_path / "index.jsonl", "w") as writer:
    writer.write_all(result)
