def averageElements(values):
    if(len(values) == 0):
        return -1
    return round(sum(values) / len(values), 2)