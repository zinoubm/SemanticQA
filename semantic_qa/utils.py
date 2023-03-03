import numpy as np


def load_prompt(path):
    with open(path) as f:
        lines = f.readlines()
        return "".join(lines)


def cosine_similarity(emb1, emb2):
    return np.dot(emb1, emb2) / (
        (np.dot(emb1, emb1) ** 0.5) * (np.dot(emb2, emb2) ** 0.5)
    )


def dot_similarity(emb1, emb2):
    return np.dot(emb1, emb2)
