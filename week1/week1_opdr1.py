def mymax(a):
    """Find the largest number in a list of integers or floats.
    
    Args
        a list: A list of integers and/or floats.
    
    Returns
    -------
    integer
        The highest number in the list.
    
    """
    assert(len(a) != 0)
    highestnumber = 0
    for number in a:
        assert(isinstance(number, (int, float)))
        if number > highestnumber:
            highestnumber = number

    return highestnumber

list = (50, 10, 2, 90, 10105231, 50, 100, 5)
print("Max of list: " + str(mymax(list)))
