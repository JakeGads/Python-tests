#Problem 2
#Write a function that combines two lists by alternatingly taking elements. For example: given the two lists [a, b, c] and [1, 2, 3], the function should return [a, 1, b, 2, c, 3].
def main():
    list1 = ['a', 'b', 'c']
    list2 = [1, 2, 3]

    lengthList1 = len(list1)
    print("The size of the first list is %d characters" % lengthList1)

    lengthList2 = len(list2)
    print("The size of the second list is %d characters" % lengthList2)

    totalLength = lengthList2 + lengthList1

    comboList = [1] * totalLength
    i = 0
    o = 1
    p = 0

    if lengthList2 <= lengthList1:

        while p < lengthList2:
            comboList[i] = list1[p]
            comboList[o] = list2[p]
            i += 2
            o += 2
            p += 1
    if lengthList1 <= lengthList2:
        while p < lengthList2:
            comboList[i] = list1[p]
            comboList[o] = list2[p]
            i += 2
            o += 2
            p += 1

    print(comboList)
