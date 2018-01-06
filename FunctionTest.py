#this is the program that will allow me to run all other programs from
#The 5 problems




run = int(input("Do you want to run Input_Tester.py (0 for no, 1 for yes)    "))
if run == 1:
    import Input_Tester
    Input_Tester.main()
    print()
    print()
    print()

run = int(input("Do you want to run Test.py (0 for no, 1 for yes)    "))
if run == 1:
    import Test
    Test.main()
    print()
    print()
    print()

run = int(input("Do you want to run The_Next_Project.py (0 for no, 1 for yes)    "))
if run == 1:
    import The_Next_Project
    The_Next_Project.main()
    print()
    print()
    print()

run = int(input("Do you want to run Problem 1.py (0 for no, 1 for yes)    "))
if run == 1:
    import Problem_1
    Problem_1.main()
    print()
    print()
    print()

run = int(input("Do you want to run Problem 2.py (0 for no, 1 for yes)    "))
if run == 1:
    import Problem_2
    Problem_2.main()
    print()
    print()
    print()

run = int(input("Do you want to run Problem 3.py (0 for no, 1 for yes)    "))
if run == 1:
    import Problem_3
    Problem_3.main()
    print()
    print()
    print()