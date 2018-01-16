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

    while i < 30:
        j = randint(1, 10)
        a.append(j)
        i += 1

    a.sort()
    print(a)
    def Constrution():
        b = []
        i = 0
        k = 0
        while i < len(a):
            j = a[i]
            if len(a) > i + 1:
                k = a[i + 1]
            else:
                k = 0
            if j == k:
                b.append(k)
            i += 1
        i = 0
        k = 0
        while i < len(a):
            while k < len(b):
                if b[k] == a[i]:
                    a.pop(i)
                k += 1
            k = 0
            i += 1
        print(b)
        print(a)
    def Set():
        b = set(a)
        print(b)


    Constrution()
    print()
    print()
    print()
    Set()

main()