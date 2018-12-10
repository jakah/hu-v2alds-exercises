def F(n):
    """Calculate the number of possibilities to pay an amount using the coins m.

    Args:
        n (integer): The amount that must  be paid in euro cents

    Returns:
        integer: Number of possibilities.
    """
    m = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
    a = [[0 for x in range(n + 1)] for y in range(len(m))]
    for i in range(len(a)):
        a[i][0] = 1
        for j in range(len(a[i])):
            a[0][j] = 1
            if j >= m[i]:
                a[i][j] = a[i - 1][j] + a[i][j - m[i]]
            elif j < m[i]:
                a[i][j] = a[i - 1][j]

    return a[len(m) - 1][n]


print(F(7))
