import os
from pathlib import Path

from index import IndexSearchEngine
from gpt_3_manager import Gpt3Manager

from dotenv import load_dotenv
from chat import ChatBot
from index import JsonLinesIndex

from prompt import TextPromptLoader

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def test_chatbot():
    path = Path("index") / "index.jsonl"

    index = JsonLinesIndex()
    loaded = index.load(path)
    gpt_manager = Gpt3Manager(api_key=OPENAI_API_KEY)

    engine = IndexSearchEngine(loaded, gpt_manager=gpt_manager)
    loader = TextPromptLoader()
    chatbot = ChatBot(engine, prompt_loader=loader, gpt_manager=gpt_manager)

    answer = chatbot.ask("What does the twitter terms of service does")

    assert answer != None
