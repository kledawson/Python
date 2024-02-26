import random

def invoice(unitPrice, quantity, shipping=10, handling=5):
    cost = unitPrice * quantity
    total = cost + shipping + handling
    print(f"Cost (unitPrice x quantity) = {cost}")
    print(f"Shipping = {shipping}")
    print(f"Handling = {handling}")
    print(f"Total = {total}")

def printGroupMembers(group_name, *students):
    print(f"Members of {group_name}")
    for student in students:
        print(student)

def overseerSystem(kwargs):
    if 'temperature' in kwargs and kwargs['temperature'] > 500:
        print(f"Warning: temperature is {kwargs['temperature']}")
    if 'CO2level' in kwargs and kwargs['CO2level'] > 0.15:
        print(f"Warning: CO2level is {kwargs['CO2level']}")
    if 'miscError' in kwargs:
        print(f"Misc error #{kwargs['miscError']}")



if __name__ == '__main__':
    invoice(20, 4, shipping=8)
    print(" ")
    invoice(15, 3, handling=15)
    print(" ")
    printGroupMembers("Group A", "Li", "Audry", "Jia")
    print(" ")
    printGroupMembers("Group B", "Sasha", "Migel", "Tanya", "Hiroto")
    print(" ")
    message1 = {'temperature': 550}
    message2 = {'temperature': 475}
    message3 = {'temperature': 450, 'miscError': 404}
    message4 = {'CO2level': 0.17}
    message5 = {'CO2level': 0.2, 'miscError': 418} 
    overseerSystem(message1)
    overseerSystem(message2)
    overseerSystem(message3)
    overseerSystem(message4)
    overseerSystem(message5)
    print(" ")

def out():
    print("Out")
    return 0

def single():
    print("Single")
    return 1

def double():
    print("Double")
    return 2

def triple():
    print("Triple")
    return 3

def homerun():
    print("Home Run")
    return 4

outcomes = [out, single, double, triple, homerun]

probabilities = [70, 18, 5, 1, 6]

outs = 0
score = 0

while outs < 3:
    outcome = random.choices(outcomes, weights=probabilities, k=1)[0]
    if outcome == out:
        outs += 1
    outcome()

'''Execution results:
Cost (unitPrice x quantity) = 80
Shipping = 8
Handling = 5
Total = 93

Cost (unitPrice x quantity) = 45
Shipping = 10
Handling = 15
Total = 70

Members of Group A
Li
Audry
Jia

Members of Group B
Sasha
Migel
Tanya
Hiroto

Warning: temperature is 550
Misc error #404
Warning: CO2level is 0.17
Warning: CO2level is 0.2
Misc error #418

Out
Single
Out
Single
Home Run
Out'''

print("end of program.")