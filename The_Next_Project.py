def main():
    print("We are now in the main fuction")
    def text():
        print("Now we are in the text function")
        s = input("Please enter your text       ")
        return s
    def printText(str):
        print("and now we are in the printTextFunction")
        print("your text string is '%s'" % s)


    s = text()
    printText(s)






