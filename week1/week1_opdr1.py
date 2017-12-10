'''
    File name: week1_opdr1.py
    Author: Jari van Dam
    Studentnumber: 1677046
    Group: V2C/retake
    Teacher: Frits Dannenberg
'''


def mymax(a):
    """Find the largest number in a list of integers or floats.
    
    Args
        a itterable: A list of integers and/or floats.
    
    Returns
    -------
    itterable type
        The highest value in the list.
    
    """
    assert(len(a) != 0)
    highestnumber = a[0]
    for number in a:
        assert(isinstance(number, (int, float)))
        if number > highestnumber:
            highestnumber = number

    return highestnumber

list = (50, 10, 2, 90, 10105231, 50, 100, 5)
print("Max of list: " + str(mymax(list)))
