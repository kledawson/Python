import csv

with open('ZenOfPython.txt', 'w') as file:
    file.write("Beautiful is better than ugly.\n")
    file.write("Explicit is better than implicit.\n")

with open('ZenOfPython.txt', 'a') as file:
    file.write("Readability counts.\n")
    file.write("If the implementation is hard to explain, it's a bad idea.\n")

with open('ZenOfPython.txt', 'r') as file:
    print(file.read())


city_dict = {}

with open('Cities.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        city_dict[(row['City'], row['State'])] = int(row['Population'])

for city_state, population in city_dict.items():
    print(city_state[0], city_state[1], population)

city = input('Please enter a city: ')
state = input('Please enter a state: ')
if (city, state) in city_dict:
    print(f"{city} {state} has a population of {city_dict[(city, state)]}")
else:
    print(f"{city} {state} is not in the list.")