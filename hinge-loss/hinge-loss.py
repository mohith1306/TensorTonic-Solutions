import numpy as np

def hinge_loss(y_true: list, y_score: list, margin: float = 1.0, reduction: str = "mean") -> float:
    """
    Returns the loss as a float.
    """
    # Write code here
    ans=[]
    for i in range(len(y_true)):
        ans.append(max(0, margin - y_true[i] * y_score[i]))

    if reduction == "mean":
        return sum(ans) / len(ans)
    else:
        return sum(ans)
    pass