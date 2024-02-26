'''
Dawson Le
CIS 41A   Winter 2023
Unit B, Problem B
'''

SMALL_BEAD_PRICE = 10.20
MEDIUM_BEAD_PRICE = 8.52
LARGE_BEAD_PRICE = 7.98

small_beads = int(input("How many boxes of small beads do you need? "))
medium_beads = int(input("How many boxes of medium beads do you need? "))
large_beads = int(input("How many boxes of large beads do you need? "))

print("SIZE \t\t\t Quantity \t COST PER BOX \t\t TOTALS")
print("Small Beads \t\t{:>6} \t\t ${:>9.2f} \t\t ${:>9.2f}".format(small_beads, SMALL_BEAD_PRICE, small_beads * SMALL_BEAD_PRICE))
print("Medium Beads \t\t{:>6} \t\t ${:>9.2f} \t\t ${:>9.2f}".format(medium_beads, MEDIUM_BEAD_PRICE, medium_beads * MEDIUM_BEAD_PRICE))
print("Large Beads \t\t{:>6} \t\t ${:>9.2f} \t\t ${:>9.2f}".format(large_beads, LARGE_BEAD_PRICE, large_beads * LARGE_BEAD_PRICE))

"""
How many boxes of small beads do you need? 10
How many boxes of medium beads do you need? 9
How many boxes of large beads do you need? 8
SIZE                     Quantity        COST PER BOX            TOTALS
Small Beads                 10           $    10.20              $   102.00
Medium Beads                 9           $     8.52              $    76.68
Large Beads                  8           $     7.98              $    63.84

How many boxes of small beads do you need? 5
How many boxes of medium beads do you need? 10
How many boxes of large beads do you need? 15
SIZE                     Quantity        COST PER BOX            TOTALS
Small Beads                  5           $    10.20              $    51.00
Medium Beads                10           $     8.52              $    85.20
Large Beads                 15           $     7.98              $   119.70
"""
print("end of program.")