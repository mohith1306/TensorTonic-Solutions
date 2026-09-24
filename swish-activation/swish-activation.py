import numpy as np

def swish(x: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    ans=[]
    for i in x:
        if isinstance(i,list):
            ans.append(swish(i))
        else:
            ans.append(i*(1/(1+np.exp(-1*i))))
    return np.array(ans)
    pass