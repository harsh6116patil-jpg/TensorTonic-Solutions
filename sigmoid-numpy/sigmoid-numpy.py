import numpy as np

def sigmoid(x):
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code her
    x = np.asarray(x,dtype = int)
    return 1/(1+np.exp(-x))