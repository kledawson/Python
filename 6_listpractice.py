list1 = []

list1.extend([1,3,5])

list1[1], list1[2] = list1[2], list1[1]

print("Items in list1:")
for item in list1:
    print(item)

list2 = [1, 2, 3, 4]

list3 = list1 + list2

print("\nlist3 is:", list3)

print("list3 contains a 3:", 3 in list3)

count = list3.count(3)
print("list3 contains", count, "3s")

index = list3.index(3)
print("The index of the first 3 contained in list3 is", index)

first3 = list3.pop(index)
print("first3 =", first3)

print("\nlist3 is now:", list3)

list4 = sorted(list3)

print("\nlist4 is:", list4)

middle_slice = list3[index-1:index+2]
print("Slice of list3 is:", middle_slice)

length = len(list3)
print("\nLength of list3 is", length)

max_value = max(list3)
print("The max value in list3 is", max_value)

list3.sort()
print("\nSorted list3 is:", list3)

list5 = [list1, list2]

print("\nlist5 is:", list5)

print("Value 4 from list5:", list5[1][3])

'''Example output:
Items in list1:
1
5
3

list3 is: [1, 5, 3, 1, 2, 3, 4]
list3 contains a 3: True
list3 contains 2 3s
The index of the first 3 contained in list3 is 2
first3 = 3

list3 is now: [1, 5, 1, 2, 3, 4]

list4 is: [1, 1, 2, 3, 4, 5]
Slice of list3 is: [5, 1, 2]

Length of list3 is 6
The max value in list3 is 5

Sorted list3 is: [1, 1, 2, 3, 4, 5]

list5 is: [[1, 5, 3], [1, 2, 3, 4]]
Value 4 from list5: 4'''

print("end of program.")
