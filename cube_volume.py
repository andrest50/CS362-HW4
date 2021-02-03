
"""
Function for calculating volume of a cube
-Return value of -1 is an error
"""
def cubeVolume(length, width, height):

    #No strings allowed
    if(isinstance(length, str) or isinstance(width, str) or isinstance(height, str) ):
        return -1

    #No negative values allowed
    if(length < 0 or width < 0 or height < 0):
        return -1

    return round(length * width * height, 2)