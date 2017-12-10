import random


def hashcollision(lookuptable, start, end, step):
    """Create a dictionary with all numbers and hash values. And check if two numbers have the same hash. Print the collision when one occurs. 

    Args:
        lookuptable (dictionary): Empty dictionary where the hash table will be stored in.
        start (float): Starting number
        end (float): End number
        step (float): Steps between the numbers.

    Returns:
        boolean: True when a collision has occurred, otherwise False.
    """
    number = start
    running = True
    while number < end and running:
        storehash = hash(number)
        if storehash in lookuptable:
            print("duplicate")
            print(repr(number))
            print("and")
            number2 = lookuptable[storehash]
            print(repr(number2))
            running = False
            return True
        else:
            lookuptable[storehash] = number
        number += step
    return False
lookuptable = {}

hashcollision(lookuptable, 0.0, 1.0, 0.0000000000000001)
