"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists
(without duplicates). Make sure your program works on two lists of different sizes.
"""
from random import *
def main():
    def determinedlists():
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        c = []
        w = 0
        i = 0
        h = 0
        if len(a) > len(b):  # if a is greater
            w = len(a)
            h = len(b)
            y = h
            while y < w:
                b.append(0)
                y += 1
        else:  # if b is greater
            w = len(b)
            h = len(a)
            y = h
            while y < w:
                a.append(0)
                y += 1
        while i < w:
            q = 0
            while q < h:
                if a[q] == b[i]:
                    c.append(a[q])
                q += 1
            i += 1

        print("The first list:")
        print(a)
        print("The second list:")
        print(b)
        print("What they have in common:")
        print(c)
        print("What they have in common removing duplicates and moving them into numeric order")
        d = set(c)
        print(d)
    def rand():
        i = 0
        a = []
        b = []
        c = []
        while i < 200:
            j = randint(10 , 99)
            s = randint(10 , 99)
            a.append(j)
            b.append(s)
            i += 1
        if len(a) > len(b):  # if a is greater
            w = len(a)
            h = len(b)
            y = h
            while y < w:
                b.append(0)
                y += 1
        else:  # if b is greater
            w = len(b)
            h = len(a)
            y = h
            while y < w:
                a.append(0)
                y += 1
        i = 0
        while i < w:
            q = 0
            while q < h:
                if a[q] == b[i]:
                    c.append(a[q])
                q += 1
            i += 1

        print("The first list:")
        print(a)
        print("The second list:")
        print(b)
        print("What they have in common:")
        print(c)
        print("What they have in common removing duplicates and moving them into numeric order")
        d = set(c)
        print(d)
    determinedlists()
    print()
    print()
    print()
    print()
    print()
    rand()

main()