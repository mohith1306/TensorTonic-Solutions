import numpy as np
def compute(i):
    return (np.exp(i)-np.exp(-i))/(np.exp(i)+np.exp(-i))
def tanh(x: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    ans=[]
    for i in x:
        if isinstance(i,list):
            ans.append(tanh(i))
        else:
            ans.append(compute(i))
    return np.array(ans)
    pass