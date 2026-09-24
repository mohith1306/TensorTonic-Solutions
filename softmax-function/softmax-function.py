import numpy as np

def func(x):
    maxx = max(x)
    sum = 0
    ans = []
    for i in x:
        sum += np.exp(i - maxx)
    for i in x:
        ans.append(np.exp(i - maxx) / sum)
    return ans


def softmax(x: list) -> np.ndarray:
    """
    Returns stable softmax probabilities as a NumPy array matching the shape of x.
    """
    ans = []
    for i in x:
        if isinstance(i, list):
            ans.append(func(i))
        else:
            return np.array(func(x))
    return np.array(ans)