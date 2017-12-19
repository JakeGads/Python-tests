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
