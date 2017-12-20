#this is the program that will allow me to run all other programs from
#The 5 problems


#Problem 2
#Write a function that combines two lists by alternatingly taking elements. For example: given the two lists [a, b, c] and [1, 2, 3], the function should return [a, 1, b, 2, c, 3].


run = int(input("Do you want to run Input_Tester.py (0 for no, 1 for yes)    "))
if run == 1:
    import Input_Tester
    Input_Tester.main()

run = int(input("Do you want to run Test.py (0 for no, 1 for yes)    "))
if run == 1:
    import Test
    Test.main()

run = int(input("Do you want to run The_Next_Project.py (0 for no, 1 for yes)    "))
if run == 1:
    import The_Next_Project
    The_Next_Project.main()

