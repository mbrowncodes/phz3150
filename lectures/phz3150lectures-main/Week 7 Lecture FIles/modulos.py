import numpy as np

[ 2, -4, 10, 32, 40, 27, 20, 31 ]
def modulos_ten(list):
    """
    This returns the value of the list of whole numbers
    that are divisible by 10.
    Input = list of numbers
    Output = sublist of numbers divisible my 10
    """
    sublist = []
    
    #index i:

    for i in range(len(list)):
    
        if list[i] % 10 == 0:
            sublist.append(list[i])

    if len(sublist) == 0:
        print("None of the elements were divisible by ten!")
        return None
    else:
        return sublist

