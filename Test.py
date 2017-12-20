# This is where I list the functions

def main():
    def Jake():
        print("Holy Guacamoli this is a pythonian function")

    def Test():
        print("This is a test line")  # standard output like a cout
        x = 1  # no need to specify class
        if x == 1:
            print('x currently equals one')
        else:
            print('x does not currently equal one')
        print(x)

        y = float(1)  # will set a class if not defined class will be auto set
        print(y)

        a, b = 4, 5
        print(a, " ", b)

        # This will not work! You cannot mix types
        one = 1
        two = 2
        hello = "hello"

        # print(one + two + hello)

        # this is a list not an array
        print("   hello      "  # there is no endline this just prints with spaces
              "   from      "
              "   the      "
              "   other      "
              "   side      "
              "         ")
        mylist = []
        mylist.append(1)
        mylist.append(2)
        mylist.append(3)
        print(mylist[0])  # prints 1
        print(mylist[1])  # prints 2
        print(mylist[2])  # prints 3

        # prints out 1,2,3
        for x in mylist:
            print(x)
        print()
        print()
        print()

        jlist = []
        jlist.append('reddit')
        jlist.append('is')
        jlist.append('fun')
        for x in jlist:
            print(x)

        print()
        print()
        print()

        glist = [1, 2, 3]
        print(glist[1], " ", glist[2], " ", glist[0])

        numbers = [1, 2, 3]
        names = ["John", "Eric", "Jessica"]
        strings = [names[0], names[1], names[2]]

        # write your code here
        second_name = strings[1]

        # this code should write out the filled arrays and the second name in the names list (Eric).
        print(numbers[0], "         ", numbers[1], "        ", numbers[2])
        print(strings[0], "         ", strings[1], "        ", strings[2])
        print("The second name on the names list is %s" % second_name)

        jnum = 5 ** 2  # 5 to the 2nd power
        print(jnum)

        gnum = 2 ** 3  # 2 to the 3rd power
        print(gnum)

        # %s - String (or any object with a string representation, like numbers)

        # %d - Integers

        # %f - Floating point numbers

        # %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

        # %x/%X - Integers in hex representation (lowercase/uppercase)

        name = "John"
        print("Hello, %s!" % name)

        o = "world"
        print("Hello  %s" % o)

        name = "John"
        age = 23
        print("%s is %d years old." % (name, age))

        astring = "Hello world!"
        print(astring[::-1])  # will print a string backwords becuase of all of the pratical applications of that

        astring = "Hello world!"
        print(astring.upper())  # sets all letters to UPPERCASE
        print(astring.lower())  # sets all letters to lowercase

        afewwords = astring.split(" ") #split up the  words to read indivudal notations
        print(afewwords)
        print(afewwords[0]) # prints the nth letter in the array

        print("")
        print("")
        print("")
        print("")
        #booleans
        x = 3
        print(x == 2) #will be false
        print(x == 3) #will be true
        print(x < 3)
        print("")
        print("")
        print("")
        print("")

        name = "Jake Gadaleta"
        age = 19
        if name == "Jake Gadaleta" and age == 19:
            print("your name is %s and your age is %d" % (name, age))
        if x == 3:
            print(x)
        print("")
        print("")
        print("")
        print("")

        # how to check lists
        name = "Jacob"
        if name in ["John", "Jacob", "Jinkkimhere", "Smith"]:
            print("are you the John Jacoob Jinkimhemere Smith")
            print("cause his name is my name too")

        x = [1,2,3]
        y = [1,2,3]
        print(x == y) # Prints out True
        print(x is y) # Prints out False
        print(x is x) # Prints out True

        print("")
        print("")
        print("")
        print("")

        number = 20
        second_number = 10
        first_array = [1,2,3]
        second_array = [1,2,3]

        if number > 15:
            print("1")

        if first_array == second_array:
            print("2")

        if len(second_array) == 3:
            print("3")

        if len(first_array) + len(second_array) == 4:       #len() is length measurment
            print("4")

        if first_array and first_array[0] == 1:             #When set like this an array will only read the firs vaule
            print("5")

        if not second_number == 1:
            print("6")

        print("")
        print("")
        print("")
        print("")

        #loops
        primes = [2, 3, 5, 7, 10, 6]
        for prime in primes:
            print(prime)

        primes = [4, 5]
        for prime in primes:
            print(prime)

        print("")
        print("")
        print("")
        print("")

        # Prints out the numbers 0,1,2,3,4
        for x in range(5):
            print(x)

        print("")
        print("")
        print("")
        print("")

        # Prints out 3,4,5
        for x in range(3, 6):
            print(x)

        print("")
        print("")
        print("")
        print("")

        # Prints out 3,5,7
        for x in range(3, 8, 2):
            print(x)


        print("")
        print("")
        print("")
        print("")

        count = 0
        while True:
            print(count)
            count += 1
            if count >= 5:
                break

        # Prints out only odd numbers - 1,3,5,7,9
        for x in range(10):
            # Check if x is even
            if x % 2 == 0:
                continue
            print(x)

        print("")
        print("")
        print("")
        print("")

        count=0
        while(count<5):
            print(count)
            count +=1
        else:
            print("count value reached %d" %(count))

        # Prints out 1,2,3,4
        for i in range(1, 10):
            if(i%5==0):
                break
            print(i)
        else:
            print("this is not printed because for loop is terminated because of break but not due to fail in condition")

        print("")
        print("")
        print("")
        print("")



    # This is where the functions get called from
    Test()
    Jake()


