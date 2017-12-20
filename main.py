#this is the program that will allow me to run all other programs from

run = int(input("Do you want to run Input_Tester.py (0 for no, 1 for yes)    "))
if run == 1:
    import Input_Tester
    Input_Tester.main()

run = int(input("Do you want to run Test.py (0 for no, 1 for yes)    "))
if run == 1:
    import Test
    Test.main()
