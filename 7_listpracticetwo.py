list1 = [2, 4.1, 'hello']

list2 = list1

import copy
list3 = copy.deepcopy(list1)

print(list1 == list2)
print(list1 == list3)
print(list2 == list3)

print(list1 is list2)
print(list1 is list3)
print(list2 is list3)

print(id(list1))
print(id(list2))
print(id(list3))

list1.append(8)

list2.insert(1, 'goodbye')

list3.pop(0)

print(list1) 
print(list2) 
print(list3) 

'''True
True
True
True
False
False
2495905511488
2495905511488
2495898329920
[2, 'goodbye', 4.1, 'hello', 8]
[2, 'goodbye', 4.1, 'hello', 8]
[4.1, 'hello']'''

print("Results match, end of program.")