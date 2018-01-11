"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
"""

def main():
    run = 1
    while run == 1:
        num = int(input("Enter a number and the computer will tell you if it is even or not     "))
        EoO = num % 2
        if EoO == 0:
            print("%d is a even number" % num)
        else:
            print("%d is an odd number" % num)
        run = int(input("If you want to run this again type 1 to quit type anything else"))


main()