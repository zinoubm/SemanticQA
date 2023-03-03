from abc import ABC, abstractmethod
import jsonlines
from TwitterChatBot.utils import dot_similarity


class Index(ABC):
    @abstractmethod
    def load(self, path):
        pass


class JsonLinesIndex(Index):
    def load(self, path):
        with jsonlines.open(path) as passages:
            indexes = list(passages)
        return indexes


class IndexSearchEngine:
    def __init__(self, indexes, gpt_manager):
        self.indexes = indexes
        self.gpt_manager = gpt_manager

    def search(self, question, count=4):
        question_embedding = self.gpt_manager.get_embedding(prompt=question)

        simmilarities = []
        for index in self.indexes:
            embedding = index["embedding"]
            score = dot_similarity(question_embedding, embedding)
            simmilarities.append({"index": index, "score": score})

            sorted_similarities = sorted(
                simmilarities, key=lambda x: x["score"], reverse=True
            )

        return [result["index"]["content"] for result in sorted_similarities[:count]]
