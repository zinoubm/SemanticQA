import os
from pathlib import Path
from dotenv import load_dotenv

from TwitterChatBot.index import IndexSearchEngine
from TwitterChatBot.gpt_3_manager import Gpt3Manager
from TwitterChatBot.chat import ChatBot
from TwitterChatBot.index import JsonLinesIndex
from TwitterChatBot.prompt import TextPromptLoader

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

path = Path("../index") / "index.jsonl"


def ask(question):
    index = JsonLinesIndex()
    loaded = index.load(path)
    gpt_manager = Gpt3Manager(api_key=OPENAI_API_KEY)

    engine = IndexSearchEngine(loaded, gpt_manager=gpt_manager)
    loader = TextPromptLoader()
    chatbot = ChatBot(engine, prompt_loader=loader, gpt_manager=gpt_manager)

    answer = chatbot.ask(question)
    return answer
