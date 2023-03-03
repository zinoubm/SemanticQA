import openai


class Gpt3Manager:
    def __init__(self, api_key):
        openai.api_key = api_key

    def get_completion(self, prompt, max_tokens=128, model="text-davinci-003"):
        response = None
        try:
            response = openai.Completion.create(
                prompt=prompt,
                max_tokens=max_tokens,
                model=model,
            )["choices"][0]["text"]

        except Exception as err:
            print(f"Sorry, There was a problem \n\n {err}")

        return response

    def get_embedding(self, prompt, model="text-similarity-ada-001"):
        prompt = prompt.replace("\n", " ")
        embedding = None
        try:
            embedding = openai.Embedding.create(input=[prompt], model=model)["data"][0][
                "embedding"
            ]
        except Exception as err:
            print(f"Sorry, There was a problem {err}")

        return embedding
