"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous
two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""
def main():
    fibonnaci = [0]
    fibonnaci.append(1)
    x = 0
    p = 1
    i = 0
    usernum = int(input("How many Fibonnaci numbers do you want to calculate         "))
    while x < usernum:
        x += 1
        q = fibonnaci[p] + fibonnaci[i]
        fibonnaci.append(q)
        p += 1
        i = p - 1

    w = 0
    k = 0
    c = 0

    while w < usernum + 1:
        w += 10
        k = w - 10
        print(fibonnaci[k:w])
        c += 1


main()