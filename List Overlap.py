"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists
(without duplicates). Make sure your program works on two lists of different sizes.
"""

def main():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = []
    w = 0
    i = 0
    h = 0
    if len(a) > len(b): #if a is greater
        w = len(a)
        h = len(b)
        y = h
        while y < w:
            b.append(0)
            y += 1
    else:               #if b is greater
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
    i = 0

    while i <= w:
        if i + 1 < w:
            if c[i] == c[i + 1]:
                del c[i]
            i += 1
    print("The first list:")
    print(a)
    print("The second list")
    print(b)
    print("What they have in common")
    print(c)
main()