from pathlib import Path
from utils import load_prompt


def test_load_prompt_default():
    path = Path("prompts") / "question_answering.txt"

    with open(path) as f:
        lines = f.readlines()
        testing_prompt = "".join(lines)

    prompt = load_prompt(path)

    assert prompt == testing_prompt
