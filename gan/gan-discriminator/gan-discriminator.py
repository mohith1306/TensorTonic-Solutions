import numpy as np

def discriminator(x: np.ndarray, W: np.ndarray) -> np.ndarray:
    """
    Returns discriminator probabilities as a float64 array with shape (B, 1).
    """
    x=np.asarray(x)
    W=np.asarray(W)
    X=x@W
    return 1.0/(1.0+np.exp(-X))
    pass