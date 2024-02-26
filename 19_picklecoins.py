class BritCoins:
    __coinValues = {"pound":240, "shilling":12, "penny":1}

    def __init__(self, **kwargs):
        self.totalPennies = 0
        for coinType, coinQty in kwargs.items():
            self.totalPennies += coinQty * self.__coinValues[coinType]

    def __add__(self, other):
        total = self.totalPennies + other.totalPennies
        return BritCoins(penny=total)

    def __sub__(self, other):
        total = self.totalPennies - other.totalPennies
        return BritCoins(penny=total)

    def __str__(self):
        total = self.totalPennies
        coinStr = ""
        for coinType in self.__coinValues:
            coinQty = total // self.__coinValues[coinType]
            total -= coinQty * self.__coinValues[coinType]
            if coinQty > 0:
                coinStr += str(coinQty) + " " + coinType
                if coinQty > 1:
                    coinStr += "s"
                coinStr += " "
        if coinStr == "":
            coinStr = "0 pennies"
        return coinStr.strip()
    
c1 = BritCoins(pound=4, shilling=24, penny=3)
c2 = BritCoins(pound=3, shilling=4, penny=5)
c3 = c1 + c2
c4 = c1 - c2

print("c1 =", c1)
print("c2 =", c2)
print("c3 =", c3)
print("c4 =", c4)

import pickle

with open("britcoins.pickle", "wb") as f:
    pickle.dump(c4, f)

with open("britcoins.pickle", "rb") as f:
    c5 = pickle.load(f)

print("c5 = ", c5) 

'''Execution results:
c1 = 5 pounds 4 shillings 3 pennys
c2 = 3 pounds 4 shillings 5 pennys
c3 = 8 pounds 8 shillings 8 pennys
c4 = 1 pound 19 shillings 10 pennys
c5 =  1 pound 19 shillings 10 pennys'''

print("end of program.")