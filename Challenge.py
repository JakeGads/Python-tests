"""
Given a string and a non-negative int n, return a larger string that is n copies of the original string.
"""

def Stringy():
    string = input("What would you like to print")
    num = int(input("How many times do you want to print it"))
    string *= num
    return string
def main(string):
    print(string)


stringy = Stringy()
main(stringy)
