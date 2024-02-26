quote = "Believe you can and you're halfway there."
count = quote.count("a")
print("The number of 'a' characters are:", count)
for i in range(count):
    index = quote.find("a")
    print("a is found at index:", index)
    quote = quote[index + 1:]


num_rows = int(input("Please enter the number of rows for the multiplication table: "))
counter = 1
for i in range(1, num_rows + 1):
    row = ""  
    for j in range(1, i + 1):
        product = i * j  
        row += f"{product:4d}"  
    print(row)

'''Example output:
The number of 'a' characters are: 4
a is found at index: 13
a is found at index: 2
a is found at index: 11
a is found at index: 3
Please enter the number of rows for the multiplication table: 12
   1
   2   4
   3   6   9
   4   8  12  16
   5  10  15  20  25
   6  12  18  24  30  36
   7  14  21  28  35  42  49
   8  16  24  32  40  48  56  64
   9  18  27  36  45  54  63  72  81
  10  20  30  40  50  60  70  80  90 100
  11  22  33  44  55  66  77  88  99 110 121
  12  24  36  48  60  72  84  96 108 120 132 144
'''

print("end of program.")