def getnumbers(s):
    """Get all the numbers from a string

    Args:
        s string: The string were the numbers are in

    Returns:
        dictionary: All numbers found in the string
    """
    numbers = []
    lastchar = 'a'
    currentnumber = 0
    for item in s:
        try:
            number = int(item)
            if (lastchar != 'a'):
                currentnumber *= 10
                currentnumber += number
                lastchar = number
            else:
                currentnumber = number
                lastchar = number
        except ValueError:
            if(lastchar != 'a' and currentnumber != 0):
                numbers.append(currentnumber)
                currentnumber = 0
    if (currentnumber != 0):
        numbers.append(currentnumber)
        currentnumber = 0

    return numbers
