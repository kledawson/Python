string = input("Enter a string: ")

result = string.isupper()
print("Is string in uppercase? ", result)

result = string.isdigit()
print("Is string all digits? ", result)

result = string.isalpha()
print("Is string all alphabets? ", result)

text = "Type, type, type away.\nCompile. Run. Hip hip hooray!\nNo error today!"
print(text)

quote = "And now for something completely different"

print(quote[:6])

print(quote[-4:])

print(quote[14:16])

print(quote[::2])

print(quote[::-1])

pattern1 = ".~*'"

pattern2 = pattern1 + pattern1[::-1]

print(pattern2 * 5)

'''Enter a string: ABC123
Is the string in uppercase?  True  
Is the string all digits?  False   
Is the string all alphabets?  False
Type, type, type away.
Compile. Run. Hip hip hooray!
No error today!
And no
rent
me
Adnwfrsmtigcmltl ifrn
tnereffid yletelpmoc gnihtemos rof won dnA
.~*''*~..~*''*~..~*''*~..~*''*~..~*''*~.'''

print("end of program.")