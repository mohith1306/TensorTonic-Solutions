import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    # Write code here
    pmf=[]
    for i in range(len(x)):
        if x[i]==0:
            pmf.append(1-p)
        else:
            pmf.append(p)
    mean=p
    return{
        "pmf":np.array(pmf),
        "mean":float(mean),
        "variance":float(mean*(1-mean))
    }
    pass