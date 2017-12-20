
def main():
    def InputTest():
        # this is how we run inputs
        name = input("What is your name? ")
        print("Hello, %s." % name)
        return name

    def Age(str):
        yearsOld = int(input("Hello %s what is your age  " % name))
        print(" %s your age is %d" % (name, yearsOld))
        return yearsOld

    def Year(str, ages):
        ages = ages + 1
        print("%s next year you will be %d" % (name, ages))
    name = InputTest()
    ages = Age(name)
    Year(name, ages)

