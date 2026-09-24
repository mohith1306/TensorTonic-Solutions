import math

def selu(x: list) -> list:
    """
    Returns SELU values rounded to four decimal places.
    """
    # Write code here
    ans=[]
    for i in x:
        if isinstance(i,list):
            ans.append(selu(i))
        else:
            if i>0:
                ans.append(1.0507*i)
            else:
                ans.append(1.6733*1.0507*(math.exp(i)-1))
    return ans
    pass