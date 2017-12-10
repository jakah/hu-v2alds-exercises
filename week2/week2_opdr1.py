'''
    File name: week2_opdr1.py
    Author: Jari van Dam
    Studentnumber: 1677046
    Group: V2C/retake
    Teacher: Frits Dannenberg
'''
def machtv3(a, n):
    """Summary

    Args:
        a int: the base number
        n int: the exponent

    Returns:
        int: The result of the exponentiation.
    """
    assert n > 0
    counter = 0 
    m = 1
    while n > 0:
        if n % 2 == 0:
            n = n / 2
            counter += 1
            a *= a
        else:
            n -= 1
            counter += 1
            m *= a
    print(counter)
    return m

print(machtv3(2, 10000))
