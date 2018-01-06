
#Problem 1
#Write three functions that compute the sum of the numbers in a given list using a for-loop, a while-loop, and recursion.

def main():
    aList = [1, 2, 3, 9, 25]
    def sumByWhile():
        print("We are now in the sumByWhile function")
        L = len(aList)
        i = 0
        temp = 0
        print("The length of the list is %d numbers long " % L)
        while i < L:
            temp = temp + aList[i]
            i = i + 1
            print("The sum at value #%d is %d" % (i, temp))
        print()
        print()
        print()


    def sumByFor():
        print("We are now in the sumByFor function")
        L = len(aList)
        i = 0
        temp = 0
        total = 0
        print("The length of the list is %d numbers long " % L)
        for prime in aList:
            temp = aList[i]
            total += temp
            i += 1
            print("The sum at value #%d is %d" % (i, total))

    def sumByRecursionMain(i):
        w = 0
        l = len(aList)
        if i == 0:
            temp = 0
            temp = aList[i]
            w = temp
            print("The list is %d characters long" % l)
            i = 1
            print("The sum at value #%d is %d" % (i, temp))

        temp = w
        if i <= l:
            temp += aList[i]
            i += 1
            print("The sum at value #%d is %d" % (i, temp))
        print()
        print()
        print()

    sumByWhile()
    sumByFor()