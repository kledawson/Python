name = input("Enter your name: ")

print("Uppercase name: ")

print(name.upper())

print("Name length: ")

print(len(name))

print("Fourth character of name: ")

print(name[3])

name2 = name.replace("o", "x")

print("Name 2 with all 'o' replaced with 'x's: ")

print(name2)

print("Original name: ")

print(name)

quote = "Believe you can and you're halfway there."

count = quote.count("a")

print("The number of 'a' characters are:", count)

index = quote.find("a")
while index != -1:
    print("a is found at index: ", index)
    index = quote.find("a", index + 1)

"""Enter your name: George Washington
Uppercase name:  
GEORGE WASHINGTON
Name length:     
17
Fourth character of name:
r
Name 2 with all 'o' replaced with 'x's:
Gexrge Washingtxn
Original name:
George Washington
The number of 'a' characters are: 4
a found at index:  13
a found at index:  16
a found at index:  28
a found at index:  32
"""

print("\nend")