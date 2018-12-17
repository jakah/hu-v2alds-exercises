'''
    File name: week1_opdr3.py
    Author: Jari van Dam
    Studentnumber: 1677046
    Group: V2C/retake
    Teacher: Frits Dannenberg
'''


def primecheck(maxnumber):
    """Give all primes in a list

    Args:
        numbers list: List of numbers

    Returns:
        list: List of prime numbers
    """
    numbers = [i for i in range(maxnumber)]
    primelist = [True] * maxnumber
    for i in range(2, maxnumber):
        if primelist[i]:
            j = 2
            multiple = i * 2
            while multiple <= len(primelist)-1:
                primelist[multiple] = False
                multiple = (j * i)
                j += 1

    result = []
    for i in range(len(numbers)):
        if primelist[i]:
            result.append(numbers[i])
    # Skip 0 and 1 because they are not real primes
    return result[2:]


print("List of primes under 1000")

print(primecheck(1000))
