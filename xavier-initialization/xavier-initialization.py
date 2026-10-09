import math

def xavier_initialization(W: list, fan_in: int, fan_out: int) -> list:
    """
    Returns the weights mapped to the Xavier uniform range.
    """
    # Write code here
    l=math.sqrt(6/(fan_in+fan_out))
    ans=[]
    for i in range(len(W)):
        temp=[]
        for j in range(len(W[0])):
            temp.append((W[i][j]*2*l)-l)
        ans.append(temp)
    return ans
    pass