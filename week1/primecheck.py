def checkdividableandnotself(list, checknumber):
    """Remove number from list if dividable by checknumber but not if number is checknumber

    Args:
        list list: All numbers that need to  be checked
        checknumber int: The number all values will be check against

    Returns:
        list: Description
    """
    for number in list:
        if (number % checknumber == 0 and number != checknumber):
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
