'''
    File name: week1_opdr2.py
    Author: Jari van Dam
    Studentnumber: 1677046
    Group: V2C/retake
    Teacher: Frits Dannenberg
'''
def getnumbers(s):
    """Get all the numbers from a string

    Args:
        s string: The string the numbers are in.

    Returns:
        dictionary: All numbers found in the string.
    """
    numbers = []
    lastchar_number = False
    currentnumber = 0
    for item in s:
        try:
            number = int(item)
            if (lastchar_number == True):
                currentnumber *= 10
                currentnumber += number
                lastchar_number = True
            else:
                currentnumber = number
                lastchar_number = True
        except ValueError:
            if(lastchar_number == True and currentnumber != 0):
                numbers.append(currentnumber)
                currentnumber = 0
    if (currentnumber != 0):
        numbers.append(currentnumber)
        currentnumber = 0

    return numbers

string = "een123zin45 6met-632meerdere+7777getallen"
print("Numbers in string:" + str(getnumbers(string)))