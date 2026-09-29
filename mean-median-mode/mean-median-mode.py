from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    mean = sum(x) / len(x)
    x.sort()
    n = len(x)
    if n % 2 == 0:
        median = (x[n // 2 - 1] + x[n // 2]) / 2
    else:
        median = x[n // 2]
    cnt = Counter(x)
    mode = cnt.most_common(1)[0][0]
    return {
        "mean": float(mean),
        "median": float(median),
        "mode": float(mode)
    }
    
    pass