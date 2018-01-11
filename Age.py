"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.
"""
import datetime

def main():
    now = datetime.datetime.now()
    now = now.year
    name = input(" What is your name")
    age = int(input(" What is your age"))
    till100 = now + 100 - 18
    print("Hello %s you are %d years old and in %d years you will be 100 years old" % (name, age, till100))

main()