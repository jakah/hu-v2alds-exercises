def machtv3(a, n):
    """Summary

    Args:
        a int: the base number
        n int: the exponent

    Returns:
        int: The result of the exponentiation.
    """
    assert n > 0
    m = 1
    while n > 0:
        if n % 2 == 0:
            n = n / 2
            a *= a
        else:
            n -= 1
            m *= a

    return m

print(machtv3(2, 10000))
