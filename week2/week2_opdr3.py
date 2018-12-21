'''
    File name: week2_opdr3.py
    Author: Jari van Dam
    Studentnumber: 1677046
    Group: V2C/retake
    Teacher: Frits Dannenberg
'''
from week2_opdr2 import mystack


def bracketcheck(string):
    """check if a string contains opening and closing brackets and if every opening bracket contains a closing bracket. 

    Args:
        string string: String that will be checked.

    Returns:
        boolean: True when string is correct, False when there is an error. 
    Tests:
    >>> bracketcheck('((<>)())')
    True
    >>> bracketcheck('())')
    False
    >>> bracketcheck('(>')
    False
    >>> bracketcheck('<>[][]<<<}]]()')
    False
    >>> bracketcheck('((<>))')
    True
    >>> bracketcheck('((<>)())')
    True
    >>> bracketcheck('{{}')
    False
    """
    openbrackets = ['<', '[', '(']
    closingbrackets = ['>', ']', ')']
    stack = mystack()
    for char in string:
        if char in openbrackets:
            stack.push(char)
        elif char in closingbrackets:
            try:
                stackitem = stack.pop()
            except AssertionError:
                return False
            except IndexError:
                return False
            except Exception as e:
                print(e)
            if openbrackets.index(stackitem) != closingbrackets.index(char):
                return False
        else:
            # Unkown charcter
            return False
    if stack.isEmpty():
        return True
    else:
        return False


string = "(())"
print(bracketcheck(string))
