'''
Problem 3
Write a function that computes the list of the first 100 Fibonacci numbers.
By definition, the first two numbers in the Fibonacci sequence are 0 and 1,
and each subsequent number is the sum of the previous two.
As an example, here are the first 10 Fibonnaci numbers:
0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.
'''

def main():
    fibonnaci = [0]
    fibonnaci.append(1)
    x = 0
    p = 1
    i = 0
    while x < 100:
        x += 1
        q = fibonnaci[p] + fibonnaci[i]
        fibonnaci.append(q)
        p += 1
        i = p - 1

    w = 0
    k = 0
    c = 0

    while w < 101:
        w += 10
        k = w - 10
        print(fibonnaci[k:w])
        c += 1


main()
