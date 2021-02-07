
"""
Function for concatenating into a full name
-Return value of -1 is an error
"""
def fullName(first_name, last_name):
    
    if(not(isinstance(first_name, str) and isinstance(last_name, str))):
        return -1
    
    return first_name.strip() + " " + last_name.strip()
