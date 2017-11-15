def mymax(a):
    """Find the largest number in a list of integers or floats.

    Parameters
    ----------
    a : A list of integers and/or floats.

    Returns
    -------
    integer
        The highest number in the list
    """
    assert(len(a) != 0)
    highestnumber = 0
    for number in a:
        assert(isinstance(number, (int, float)))
        if number > highestnumber:
            highestnumber = number

    return highestnumber