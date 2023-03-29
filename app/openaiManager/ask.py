from openaiManager.base import OpenAiManager


def ask(self, question):
    pass


def summarize(input: str, manager):
    prompt = f"""
    Summarize the following passage in detail
    passage: {input}

    summary:
    """

    return manager.get_chat_completion(prompt)


if __name__ == "__main__":

    test = "say hi"
    manager = OpenAiManager()
    res = manager.get_chat_completion(test, manager)
    print(res)
