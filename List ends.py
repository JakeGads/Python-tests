"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function.
"""
def main():
    a = [5, 10, 15, 20, 25]
    lenOA = len(a) - 1
    b = [a[0], a[lenOA]]
    print(a)
    print("Taking the first and last value")
    print(b)
main()