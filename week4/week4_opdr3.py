def B(n, k):
    """Calculate (n!//(k!))//(n-k)! using dynamic programming

    Args:
        n (integer): Number n
        k (integer): Number k

    Returns:
        integer: result of calculation
    """
    a = [[0 for x in range(k + 1)] for y in range(n + 1)]
    i = 0
    while i <= n:
        a[i][0] = 1
        j = 1
        while j <= k:
            a[i][j] = a[i - 1][j] + a[i - 1][j - 1]
            j += 1
        i += 1
    return a[n][k]


print(B(6, 3))
print(B(100, 50))

