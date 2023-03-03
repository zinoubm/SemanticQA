from abc import ABC, abstractmethod

# Prompt Loaders
class PromptLoader(ABC):
    @abstractmethod
    def load_prompt(self, path):
        pass


class TextPromptLoader(PromptLoader):
    def load_prompt(self, path):
        with open(path) as f:
            lines = f.readlines()
            return "".join(lines)


# Prompts
class Prompt(ABC):
    def __init__(self, prompt_loader: PromptLoader):
        self.prompt_loader = prompt_loader

    def load_prompt(self, path):
        return self.prompt_loader.load_prompt(path)

    @abstractmethod
    def load(self, path):
        pass


class QuestionAnsweringPrompt(Prompt):
    def __init__(self, passage, question, prompt_loader):
        super().__init__(prompt_loader=prompt_loader)
        self.passage = passage
        self.question = question

    # trust me, you'll need this later
    # .replace("<<PASSAGE>>", self.result["index"]["content"])

    def load(self, path):
        prompt = (
            self.load_prompt(path)
            .replace("<<PASSAGE>>", self.passage)
            .replace("<<QUESTION>>", self.question)
        )
        return prompt


class PassageSummarizationPrompt(Prompt):
    def __init__(self, passage, prompt_loader):
        super().__init__(prompt_loader=prompt_loader)
        self.passage = passage

    # prompt = self.load_prompt(path).replace("<<PASSAGE>>", )

    def load(self, path):
        prompt = self.load_prompt(path).replace("<<PASSAGE>>", self.passage)
        return prompt
