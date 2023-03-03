import os
import openai
from pathlib import Path

from TwitterChatBot.index import IndexSearchEngine
from TwitterChatBot.prompt import (
    QuestionAnsweringPrompt,
    PassageSummarizationPrompt,
    TextPromptLoader,
)


openai.api_key = OPENAI_API_KEY


class ChatBot:
    def __init__(
        self, index_search_engine: IndexSearchEngine, prompt_loader, gpt_manager
    ):
        self.index_search_engine = index_search_engine
        self.prompet_loader = prompt_loader
        self.gpt_manager = gpt_manager

    def ask(self, question):
        search_result = self.index_search_engine.search(question=question, count=2)

        answers = []
        for result in search_result:
            question_answering_prompt = QuestionAnsweringPrompt(
                passage=result, question=question, prompt_loader=self.prompet_loader
            )
            prompt = question_answering_prompt.load(
                Path("../prompts") / "question_answering.txt"
            )

            answer = self.gpt_manager.get_completion(
                prompt=prompt, max_tokens=80, model="text-curie-001"
            )
            answers.append(answer)

        passage_summarization_prompt = PassageSummarizationPrompt(
            "\n".join(answers), self.prompet_loader
        )

        prompt = passage_summarization_prompt.load(
            Path("../prompts") / "passage_summarization.txt"
        )

        final_answer = self.gpt_manager.get_completion(prompt=prompt)
        return final_answer
