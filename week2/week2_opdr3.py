from week2_opdr2 import mystack


def bracketcheck(string):
    """check if a string contains opening and closing brackets and if every opening bracket contains a closing bracket. 

    Args:
        string string: String that will be checked.

    Returns:
        boolean: True when string is correct, False when there is an error. 
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
            if openbrackets.index(stackitem) != closingbrackets.index(char):
                return False
        else:
            # Unkown charcter
            return False
    return True

string = "a"
print(bracketcheck(string))
