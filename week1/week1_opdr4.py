import random

def samenumberinlist(list):
    """Check if a number occurs twice or more in a list.
    
    Args:
        list list: The list of numbers.
    
    Returns:
        boolean: True if list contains a duplicate number, else False.
    """
    duplicates = []
    itemsinlist = []
    for item in list:
        if item not in itemsinlist:
            itemsinlist.append(item)
        else:
            return True
    return False

def generaterandomlist(rangestart,rangeend,lenght):
    """Generate a list with random integers
    
    Args:
        rangestart int: The lowest random number in the list.
        rangeend int: The highest random number in the list.
        lenght int: The length of the list that will be created.
    
    Returns:
        dictionary: A list with random integers.
    """
    items = 0
    randomlist = []
    while(items < lenght):
        randomlist.append(random.randint(rangestart,rangeend))
        items+=1
    return randomlist

print("Same birthday simulation")
results = []
numberoflists = 0
numberoftrues = 0
numberoffalses = 0
while (numberoflists < 100):
    result = (samenumberinlist(
        generaterandomlist(1, 365, 23)))
    results.append(result)
    if (result == False):
        numberoftrues += 1
    else:
        numberoffalses += 1
    numberoflists += 1


print("True: " + str(numberoftrues))
print("False: " + str(numberoffalses))