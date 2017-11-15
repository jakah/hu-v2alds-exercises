import mymax
import getnumbers
import primecheck
import listoperations

print("1")
list = (50, 10, 2, 90, 10105231, 50, 100, 5)
print("Max of list: " + str(mymax.mymax(list)))
print("\n")

string = "een123zin45 6met-632meerdere+7777getallen"
print("2")
print("Numbers in string:" + str(getnumbers.getnumbers(string)))
print("\n")

print("3")
list = []
while (len(list) - 1 < 1000):
    list.append(len(list) + 1)
list.remove(1)
print("List of primes under 1000")
print(primecheck.primecheck(list))
print("\n")


print("4")
print("Same birthday simulation")
results = []
numberoflists = 0
numberoftrues = 0
numberoffalses = 0
while (numberoflists < 100):
    result = (listoperations.samenumberinlist(
        listoperations.generaterandomlist(1, 365, 23)))
    results.append(result)
    if (result == False):
        numberoftrues += 1
    else:
        numberoffalses += 1
    numberoflists += 1


print("True: " + str(numberoftrues))
print("False: " + str(numberoffalses))

print("\n")
