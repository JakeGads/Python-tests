'''
Problem 4
Write a function that given a list of non negative integers,
arranges them such that they form the largest possible number.
For example, given [50, 2, 1, 9], the largest formed number is 95021.
'''

listA = [50, 2, 10000.0, 9]
print("The List ")
print(listA)
listA.sort()
print("The List least to greatest")
print(listA)
listA.sort(reverse=True)
print("The List greatest to least")
print(listA)


listA = [55, 22, 340, 4, 99, 20]
jjj