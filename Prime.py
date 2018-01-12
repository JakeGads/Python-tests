"""
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you.
Take this opportunity to practice using functions, described below.
"""

def main():
    run = 1
    while run == 1:
        run = 0
        num = int(input("Please enter an integer (not 0,1,2)    "))
        i = 1
        truth = 0
        while i < num:
            tester = num % i
            if tester == 0:
                truth += 1
            i += 1
        if num == 2 or num == 1 or num == 0:
            print("%d is not a vaild input    " % num)
            run = 1
        else:
            if truth > 2:
                print("%d is not a prime number    " % num)
            else:
                print("%d is a prime number    " % num)

main()
