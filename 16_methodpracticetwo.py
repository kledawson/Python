def hello():
    """
    This function prints Hello World
    """
    print("Hello world")
    print("Help on function hello in module __main__:")

def printListElement(myList, index):
    try:
        print(myList[index])
    except IndexError:
        print("Error: bad index number.")

def byVal(param):
    print(f"ID of parameter in byVal {id(param)}")
    param += 7
    print(f"ID of parameter in byVal after change {id(param)}")

def byRef(param):
    print(f"ID of parameter in byRef {id(param)}")
    print(f"ID of parameter's last element in byRef {id(param[-1])}")
    param[-1] += 7
    print(f"ID of parameter in byRef after change {id(param)}")
    print(f"ID of parameter's last element in byRef after change {id(param[-1])}")

def main():
    hello()
    print(hello.__name__+"()"+hello.__doc__)

    myList = list(range(3))
    printListElement(myList, 3,)
    print(" ")

    myInt = 3
    myList = [0, 1, 2]
    print(f"ID of myInt in main is {id(myInt)}")
    print(f"ID of myList in main is {id(myList)}")
    print(f"ID of myList's last element in main is {id(myList[-1])}")
    byVal(myInt)
    byRef(myList)
    print(f"ID of myInt in main after call to byVal is {id(myInt)}")
    print(f"ID of myList in main after call to byRef is {id(myList)}")
    print(f"ID of myList's last element in main after call to byRef is {id(myList[-1])}")
    print(f"myInt is now: {myInt}")
    print(f"myList is now: {myList}")

if __name__ == '__main__':
    main()

'''Execution results:
Hello world
Help on function hello in module __main__:
hello()
    This function prints Hello World

Error: bad index number.

ID of myInt in main is 1618481250608
ID of myList in main is 1618482548992
ID of myList's last element in main is 1618481250576
ID of parameter in byVal 1618481250608
ID of parameter in byVal after change 1618481250832
ID of parameter in byRef 1618482548992
ID of parameter's last element in byRef 1618481250576
ID of parameter in byRef after change 1618482548992
ID of parameter's last element in byRef after change 1618481250800
ID of myInt in main after call to byVal is 1618481250608
ID of myList in main after call to byRef is 1618482548992
ID of myList's last element in main after call to byRef is 1618481250800
myInt is now: 3
myList is now: [0, 1, 9]'''

print("end of program.")