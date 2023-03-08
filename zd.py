from array import array
import numpy as np

def mn(num):
    a = array('i', [])
    for i in range(0, num):
        for j in range(0, num):
            a.append((i * j) % num)
    return (a)


'''x = int(input())'''
x = 5
tab = mn(x)
print(tab)
sctab = np.zeros((x, x))
for j in range(1, x):
    sctab[0][j] = tab[j]
for i in range(1, x):
    for j in range(0, x):
        sctab[i][j] = tab[(i * x) + j]
        print(tab[i * j], ' ', end="")
    print()
print()
print(sctab)

'''y = int(input())'''
y = 3
pr = 1
for i in range(1, 7):
    print(int(sctab[3][pr]))
    pr = int(sctab[3][pr])

'''for i in range(0, x):
    for j in range(0, x):
        print(tab[],' ', end="")
    print()'''
