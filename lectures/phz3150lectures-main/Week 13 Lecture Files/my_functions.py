import numpy as np #We don't actually need to use this for these functions.

def F2C(degF):
    """
    Converts degrees in F to degrees in C.
    Input: temp. in degrees F.
    Output: temp. in degrees C.
    """

    degC = 5/9*(degF - 32)
    
    return degC


def F2K(degF):
    """
    Converts degrees in F to K.
    Input: temp. in degrees F.
    Output: temp. in K.
    """
    degC = F2C(degF)
    K = degC + 273.15

    return K