dessert_dict = {
    "apple": "sauce",
    "peach": "cobbler",
    "carrot": "cake",
    "strawberry": "sorbet",
    "banana": "cream pie"
}

dessert_dict["mango"] = "sticky rice"

dessert_dict["strawberry"] = "shortcake"

del dessert_dict["carrot"]

print("apple dessert is:", dessert_dict["apple"])

print("banana dessert is:", "banana" in dessert_dict)

print("pear dessert is:", "pear" in dessert_dict)

print(dessert_dict.keys())

print(dessert_dict.values())

print(dessert_dict.items())


capitols1 = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento"
}

capitols2 = {
    "California": "Sac.",
    "Colorado": "Denver",
    "Connecticut": "Hartford"
}

capitols1.update(capitols2)

print("Sorted state capitols:",sorted(capitols1.values()))


class1 = {"Li", "Audry", "Jia", "Migel", "Tanya"}

class2 = {"Sasha", "Migel", "Tanya", "Hiroto", "Audry"}

class1.add("John")

print("Students in both classes:",sorted(class1 & class2))

print("All students:",sorted(class1 | class2))

print("Sasha is in class1:","Sasha" in class1)

'''Execution results:
apple dessert is: sauce
banana dessert is: True
pear dessert is: False
dict_keys(['apple', 'peach', 'strawberry', 'banana', 'mango'])
dict_values(['sauce', 'cobbler', 'shortcake', 'cream pie', 'sticky rice'])
dict_items([('apple', 'sauce'), ('peach', 'cobbler'), ('strawberry', 'shortcake'), ('banana', 'cream pie'), ('mango', 'sticky rice')])
Sorted state capitols: ['Denver', 'Hartford', 'Juneau', 'Little Rock', 'Montgomery', 'Phoenix', 'Sac.']
Students in both classes: ['Audry', 'Migel', 'Tanya']
All students: ['Audry', 'Hiroto', 'Jia', 'John', 'Li', 'Migel', 'Sasha', 'Tanya']
Sasha is in class1: False'''

print("end of program.")