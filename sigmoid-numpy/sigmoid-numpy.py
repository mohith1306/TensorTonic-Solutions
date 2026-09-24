import numpy as np
import math

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """

    def calculate(i):
        if i >= 0:
            return 1 / (1 + math.exp(-i))
        else:
            e = math.exp(i)
            return e / (1 + e)

    if isinstance(x, (int, float)):
        return calculate(x)

    ans = []

    for i in x:
        if isinstance(i, list):
            row = []
            for j in i:
                row.append(calculate(j))
            ans.append(row)
        else:
            ans.append(calculate(i))

    return np.array(ans)