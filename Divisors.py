"""
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""

def main():
    num = int(input("Pick a number and they will tell you all of the divisors "))
    i = 1
    a = []
    while i < num:
        saved = num % i
        if saved == 0:
            a.append(i)
        i += 1
    print(a)

main()