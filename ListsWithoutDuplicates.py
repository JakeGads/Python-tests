"""
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list
minus all the duplicates.

Extras:
    Write two different functions to do this - one using a loop and constructing a list, and another using sets.
    Go back and do Exercise 5 using sets, and write the solution for that in a different function.

"""
from random import *
def main():
    i = 0
    a = []
    while i < 10:
        j = randint(1, 10)
        a.append(j)
        i += 1
    print(a)
    def Constrution():
        b = []
        i = 0
        k = 0
        while i < len(a):
            while k < len(a):
                j = a[i]
                g = a[k]
                if j == g:
                    b.append(g)
                k += 1
            i += 1
        print(b)
    def Set():
        b = set(a)
        print(b)


    Constrution()
    print()
    print()
    print()
    Set()

main()