import openai


def get_completion(
    prompt,
    model="text-davinci-003",
    max_tokens=128,
    temperature=0,
):

    response = None
    try:
        response = openai.Completion.create(
            prompt=prompt,
            max_tokens=max_tokens,
            model=model,
            temperature=temperature,
        )["choices"][0]["text"]

    except Exception as err:
        print(f"Sorry, There was a problem \n\n {err}")

    return response


def get_chat_completion(prompt, model="gpt-3.5-turbo"):

    response = None
    try:
        response = (
            openai.ChatCompletion.create(
                model=model,
                messages=[
                    {
                        "role": "System",
                        "content": prompt,
                    }
                ],
            )
            .choices[0]
            .message
        )

    except Exception as err:
        print(f"Sorry, There was a problem \n\n {err}")

    return response


def get_embedding(prompt, model="text-similarity-ada-001"):
    prompt = prompt.replace("\n", " ")

    embedding = None
    try:
        embedding = openai.Embedding.create(input=[prompt], model=model)["data"][0][
            "embedding"
        ]

    except Exception as err:
        print(f"Sorry, There was a problem {err}")

    return embedding


if __name__ == "__main__":

    test = "say hi"
    res = get_chat_completion(test)
    print(res)
