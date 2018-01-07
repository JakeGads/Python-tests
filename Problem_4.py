'''
Problem 4
Write a function that given a list of non negative integers,
arranges them such that they form the largest possible number.
For example, given [50, 2, 1, 9], the largest formed number is 95021.
'''

def main():
    listA = [50, 2, 10, 9]
    print("The List ")
    print(listA)
    listA.sort()
    print("The List least to greatest")
    print(listA)
    listA.sort(reverse=True)
    print("The List greatest to least")
    listA.sort(reverse=True)
    print(listA)


    i = 0
    listA = [55, 22, 340, 4, 99, 20]

    while i < len(listA):
        w = 10
        while listA[i] > w:
            w *= 10
        if listA[i] > 10:
            listA[i] = listA[i] / w
            if listA[i] < 1:
                listA[i] *= 10

        i += 1

    listA.sort(reverse=True)

    print(listA)



