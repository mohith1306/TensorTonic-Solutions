import numpy as np

def relu(x) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    if isinstance(x, (int, float)):
        if x >= 0:
            return np.array(x)
        else:
            return np.array(0)

    ans = []

    for i in x:
        if isinstance(i, list):
            ans.append(relu(i))
        else:
            if i >= 0:
                ans.append(i)
            else:
                ans.append(0)

    return np.array(ans)