import math

def elu(x: list, alpha: float = 1.0) -> list:
    """
    Returns ELU applied elementwise to the input values.
    """
    # Write code here
    ans=[]
    for i in x:
        if isinstance(i,list):
            ans.append(elu(i))
        else:
            if i>0:
                ans.append(i)
            else:
                ans.append(alpha*(math.exp(i)-1))
    return ans
    pass