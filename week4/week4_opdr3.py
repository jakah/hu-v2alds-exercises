def B(n, k):
    """Calculate (n!//(k!))//(n-k)! using dynamic programming
    Args:
        n (integer): Number n
        k (integer): Number k
    Returns:
        integer: Result of calculation
    """
    a = [[0 for x in range(k + 1)] for y in range(n + 1)]
    for i in range(len(a)):
        a[i][0] = 1
        for j in range(1,k+1):
            a[i][j] = a[i - 1][j] + a[i - 1][j - 1]
    return a[n][k]



print(B(6, 3))
print(B(100, 50))
