import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    dot = 0.0
    norm_a = 0.0
    norm_b = 0.0

    for i in range(len(a)):
        dot += a[i] * b[i]
        norm_a += a[i] * a[i]
        norm_b += b[i] * b[i]

    if norm_a == 0.0 or norm_b == 0.0:
        return 0.0

    return float(dot / (np.sqrt(norm_a) * np.sqrt(norm_b)))