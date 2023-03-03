import os
from dotenv import load_dotenv
from gpt_3_manager import Gpt3Manager

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def test_gpt3_completion():
    manager = Gpt3Manager(api_key=OPENAI_API_KEY)
    request = manager.get_completion(
        prompt="This is a testing prompt", max_tokens=10, model="text-ada-001"
    )
    assert request != None


def test_gpt3_embedding():
    manager = Gpt3Manager(api_key=OPENAI_API_KEY)
    request = manager.get_embedding(prompt="This is a testing prompt")
    assert request != None
