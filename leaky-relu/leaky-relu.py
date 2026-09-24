import numpy as np



def leaky_relu(x: list | float, alpha: float = 0.01) -> np.ndarray:
    """
    Returns elementwise Leaky ReLU values as a NumPy array matching the input shape.
    """
    # Write code here
    if isinstance(x,float):
        if x>=0:
            return x
        else:
            return alpha*x
    ans=[]
    for i in x:
        if i>=0:
            ans.append(i)
        else:
            ans.append(i*alpha)
    return np.array(ans)
    pass