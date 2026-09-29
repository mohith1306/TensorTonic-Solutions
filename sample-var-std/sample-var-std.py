import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    mean=sum(x)/len(x)
    var=0.0
    for i in range(0,len(x)):
        var+=((x[i]-mean)*(x[i]-mean))
    var/=(len(x)-1)
    return{
        "variance":float(var),
        "standard_deviation":float(np.sqrt(var))
    }
    pass