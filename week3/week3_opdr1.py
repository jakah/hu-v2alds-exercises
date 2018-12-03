from itertools import permutations


def check(a, i):  # ga na of i aan a toegevoegd kan worden
    n = len(a)
    return not (i in a or  # niet in dezelfde kolom
                # niet op dezelfde diagonaal
                i+n in [a[j]+j for j in range(n)] or
                i-n in [a[j]-j for j in range(n)])  # niet op dezelfde diagonaal


def printQueens(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if a[i] == j:
                print("*", end=" ")
            else:
                print("*", end=" ")
        print()
    print()


b = []


def rsearch(N):
    global a
    global b
    for i in range(N):
        if check(a, i):
            a.append(i)
            if len(a) == N:
                b.append(a)
                # return True  # geschikte a gevonden
            else:
                if rsearch(N):
                    b.append(a)
                    return True
            del a[-1]  # verwijder laatste element
    return False


a = []  # a geeft voor iedere rij de kolompositie aan
t = 0

rsearch(8)
print(a)
printQueens(a)
print(b)

# # ===========================================================


n = 8
cols = range(n)
for vec in permutations(cols):
    if n == len(set(vec[i]+i for i in cols)) \
         == len(set(vec[i]-i for i in cols)):
        print(vec)
