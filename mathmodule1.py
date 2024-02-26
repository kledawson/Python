print("Basic numeric operations\n")

a = 3 * 2.5
print("The final value of a: ", a)

b = 2
print("The initial value of b: ", b)

b += 3
print("The final value of b: ", b)

c = 12
print("The initial value of c: ", c)

c /= 4
print("The final value of c: ", c)

d = 5 % 3
print("The final value of d: ", d)

print("\nBuilt-in functions abs, round, and min\n")

print("Absolute difference between 5 and 7 is:", abs(5 - 7))

print("3.14159 rounded to 4 decimal places is:", round(3.14159, 4))

print("186282 rounded to the nearest hundred is:", round(186282, -2))

print("The minimum of 6, -9, -3, 0 is:", min(6, -9, -3, 0))

print("\nFunctions from the math module\n")

import math

number = float(input("Enter a number: "))

sqrt = round(math.sqrt(number), 2)
print("The square root of", number, "is", sqrt)

log = round(math.log10(number), 2)
print("The base-10 log of", number, "is", log)

'''Basic numeric operations

The final value of a:  7.5
The initial value of b:  2
The final value of b:  5
The initial value of c:  12
The final value of c:  3.0
The final value of d:  2

Built-in functions abs, round, and min

Absolute difference between 5 and 7 is: 2
3.14159 rounded to 4 decimal places is: 3.1416
186282 rounded to the nearest hundred is: 186300
The minimum of 6, -9, -3, 0 is: -9

Functions from the math module

Enter a number: 7.6
The square root of 7.6 is 2.76
The base-10 log of 7.6 is 0.88'''