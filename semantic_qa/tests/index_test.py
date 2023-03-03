import os
from index import JsonLinesIndex, IndexSearchEngine
from gpt_3_manager import Gpt3Manager
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def test_jsonlines_index():
    path = Path("index") / "index.jsonl"

    index = JsonLinesIndex()
    result = index.load(path)

    assert result != None


def test_index_serach_engine():
    path = Path("index") / "index.jsonl"
    gpt_manager = Gpt3Manager(OPENAI_API_KEY)
    index = JsonLinesIndex()
    loaded = index.load(path)
    engine = IndexSearchEngine(loaded, gpt_manager=gpt_manager)

    results = engine.search(question="What does the twitter tos does")

    assert results != None
