from pathlib import Path
from prompt import QuestionAnsweringPrompt, PassageSummarizationPrompt, TextPromptLoader


def test_text_prompt_loader():
    path = Path("prompts") / "question_answering.txt"
    prompt_loader = TextPromptLoader()

    prompt = prompt_loader.load_prompt(path)
    testing_prompt = (
        "Use the passage to write a detailed answer to the following question\n"
        "\n"
        "passage: <<PASSAGE>>\n"
        "\n"
        "question: <<QUESTION>>\n"
        "\n"
        "answer:"
    )

    assert prompt == testing_prompt


def test_question_answering_prompt():
    path = Path("prompts") / "question_answering.txt"

    passage = "Hi, I'm foo and I love cycling and programming"
    question = "What is foo's hobby"

    prompt_loader = TextPromptLoader()
    prompt = QuestionAnsweringPrompt(passage, question, prompt_loader)
    loaded_prompt = prompt.load(path)

    testing_prompt = (
        "Use the passage to write a detailed answer to the following question\n"
        "\n"
        "passage: Hi, I'm foo and I love cycling and programming\n"
        "\n"
        "question: What is foo's hobby\n"
        "\n"
        "answer:"
    )

    assert loaded_prompt == testing_prompt


def test_passage_summarization_prompt():
    path = Path("prompts") / "passage_summarization.txt"

    passage = "Hi, I'm foo and I love cycling and programming"

    prompt_loader = TextPromptLoader()
    prompt = PassageSummarizationPrompt(passage, prompt_loader)
    loaded_prompt = prompt.load(path)

    testing_prompt = (
        "Summarize the following passage in detail\n"
        "passage: Hi, I'm foo and I love cycling and programming\n"
        "\n"
        "summary:"
    )

    assert loaded_prompt == testing_prompt
