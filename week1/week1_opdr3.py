def checkdividableandnotself(list, checknumber):
    """Remove number from list if dividable by checknumber but not if number is checknumber

    Args:
        list list: All numbers that need to  be checked
        checknumber int: The number all values will be check against

    Returns:
        list: Description
    """
    for number in list:
        tempnumber = number
        while ((tempnumber - checknumber) >= checknumber):
            tempnumber = tempnumber- checknumber
        if (number != checknumber and (tempnumber == 0 or tempnumber == checknumber)):
            list.remove(number)
    return list


def primecheck(numbers):
    """Give all primes in a list

    Args:
        numbers list: List of numbers

    Returns:
        list: List of prime numbers
    """
    for number in numbers:
        checkdividableandnotself(numbers, number)
    return numbers

# Create a list with numbers from 2-1000
list = []
while (len(list) < 1000):
    list.append(len(list) + 1)
list.remove(1)

print("List of primes under 1000")
print(primecheck(list))