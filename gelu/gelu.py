import math
import numpy as np

def gelu(x: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    ans=[]
    for i in x:
        if isinstance(i,list):
            ans.append(gelu(i))
        else:
            ans.append(i/2*(1+math.erf(i/math.sqrt(2))))
    return np.array(ans)
    pass
    