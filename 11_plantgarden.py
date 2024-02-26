class Plant:
    def __init__(self, name, type, height):
        self.name = name
        self.type = type
        self.height = height

class Garden:
    def __init__(self, name, plant_type, max_height):
        self.name = name
        self.plant_type = plant_type
        self.max_height = max_height
    
    def can_plant(self, plant):
        if plant.type == self.plant_type and (not self.max_height or plant.height <= self.max_height):
            return True
        return False

vegetable_garden = Garden("Vegetable Garden", "Vegetable", None)
low_garden = Garden("Low Garden", "Flower", 3)
high_garden = Garden("High Garden", "Flower", 6)

loop = True
while loop == True:
    plant = Plant(input("Please enter the plant name: "), input("Please enter the plant type: "), int(input("Please enter the plant height: ")))

    can_plant_in = []

    if vegetable_garden.can_plant(plant):
        can_plant_in.append(vegetable_garden.name)

    if low_garden.can_plant(plant):
        can_plant_in.append(low_garden.name)

    if high_garden.can_plant(plant):
        can_plant_in.append(high_garden.name)

    if len(can_plant_in) == 0:
        print("This plant does not match the criteria for any of the gardens.")
    else:
        print("A " + plant.name + " can be planted in " + " or ".join(can_plant_in) + ".")
    
    x = input("Try another plant? (Yes/No): ")
    if x.upper() == "YES":
        loop = True
    elif x.upper() == "NO":
        loop = False
    else:
        print("Not understood. Ending program...")
        loop = False

'''Example output:
Please enter the plant name: Lily
Please enter the plant type: Flower
Please enter the plant height: 3
A Lily can be planted in Low Garden or High Garden.
Try another plant? (Yes/No): Yes   
Please enter the plant name: Bonsai
Please enter the plant type: Tree
Please enter the plant height: 2
This plant does not match the criteria for any of the gardens.
Try another plant? (Yes/No): Yes
Please enter the plant name: Carrots
Please enter the plant type: Vegetable
Please enter the plant height: 1
A Carrots can be planted in Vegetable Garden.
Try another plant? (Yes/No): Yes
Please enter the plant name: Corn
Please enter the plant type: Vegetable
Please enter the plant height: 8
A Corn can be planted in Vegetable Garden.
Try another plant? (Yes/No): Yes 
Please enter the plant name: Rose
Please enter the plant type: Flower
Please enter the plant height: 5
A Rose can be planted in High Garden.
Try another plant? (Yes/No): Yes
Please enter the plant name: Sunflower
Please enter the plant type: Flower
Please enter the plant height: 8
This plant does not match the criteria for any of the gardens.
Try another plant? (Yes/No): No
'''

print("end of program.")