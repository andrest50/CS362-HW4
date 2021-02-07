
"""
Function for calculating the average of a list
-Return value of -1 is an error
"""
def averageElements(values):
    
    if(len(values) == 0):
        return -1
    
    return round(sum(values) / len(values), 2)