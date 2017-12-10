'''
    File name: week2_opdr4.py
    Author: Jari van Dam
    Studentnumber: 1677046
    Group: V2C/retake
    Teacher: Frits Dannenberg
'''
def mybin(n):
    """convert a base 10 number to a binary string. 

    Args:
        n int: Positive integer that will be converted to a binary. 

    Returns:
        String: String with binary representation of the decimal value, starting with 0b. 
    """
    assert n >= 0
    if n == 0:
        return "0b0"
    elif n == 1:
        return "0b1"
    else:
        if (n % 2 == 1 or n % 2 == 0):
            return mybin(n / 2) + str(n%2)


print(mybin(100))
