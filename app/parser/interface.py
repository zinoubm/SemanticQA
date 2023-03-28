from abc import ABC, abstractmethod


class ParserInterface(ABC):
    @abstractmethod
    def parse(file) -> str:
        pass
