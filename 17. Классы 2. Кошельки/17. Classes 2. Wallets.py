class BaseWallet:

    def __init__(self, name, amount):
        self.name =  name
        self.amount = amount 

    def __add__(self, other):
        if isinstance(other, BaseWallet):
            other = other.to_base()
        result = self.amount + other
        return BaseWallet(self.name, result)

    def __iadd__(self, other):
        if isinstance(other, BaseWallet):
            other = other.to_base()
        self.amount = self.amount + other
        return self

    def __radd__(self, other):
        return self + other

    def to_base(self):
        convert = self.amount * self.exchange_rate
        return convert

class RubbleWallet(BaseWallet):
    exchange_rate = 1

class DollarWallet(BaseWallet):
    exchange_rate = 60

class EuroWallet(BaseWallet):
    exchange_rate = 70

# тест __add__
print("тест __add__")

rub1 = RubbleWallet("Руб1", 10)
print(rub1.name, rub1.amount)

rub2 = rub1 + 20
print(rub2.name, rub2.amount)

dol1 = DollarWallet("Дол1", 10)
print(dol1.name, dol1.amount)

dol2 = dol1 + 20
print(dol2.name, dol2.amount)

euro1 = EuroWallet("Евро1", 10)
print(euro1.name, euro1.amount)

euro2 = euro1 + 20
print(euro2.name, euro2.amount)

# тест __iadd__
print("\nтест __iadd__")

rub3 = RubbleWallet("Руб3", 30)
print(rub3.name, rub3.amount)

rub3 += 20
print(rub3.name, rub3.amount)

dol3 = DollarWallet("Дол3", 30)
print(dol3.name, dol3.amount)

dol3 += 20
print(dol3.name, dol3.amount)

euro3 = EuroWallet("Евро3", 30)
print(euro3.name, euro3.amount)

euro3 += 20
print(euro3.name, euro3.amount)

# тест __radd__
print("\nтест __radd__")

rub4 = RubbleWallet("Руб4", 40)
print(rub4.name, rub4.amount)

rub5 = 50 + rub4
print(rub4.name, rub4.amount)
print(rub5.name, rub5.amount)

dol4 = DollarWallet("Дол4", 40)
print(dol4.name, dol4.amount)

dol5 = 50 + dol4
print(dol4.name, dol4.amount)
print(dol5.name, dol5.amount)

euro4 = EuroWallet("Евро4", 40)
print(euro4.name, euro4.amount)

euro5 = 50 + euro4
print(euro4.name, euro4.amount)
print(euro5.name, euro5.amount)

# тест сложение классов
print("\nтест сложение классов")

rub6 = RubbleWallet("Руб6", 60)
rub7 = RubbleWallet("Руб7", 70)
rub8 = rub6 + rub7
print(rub6.name, rub6.amount)
print(rub7.name, rub7.amount)
print(rub8.name, rub8.amount)
print(rub6.name, rub6.amount)

dol6 = DollarWallet("Дол6", 1)
rub9 = rub6 + dol6
print(rub9.name, rub9.amount)

euro6 = EuroWallet("Евро6", 1)
rub10 = rub7 + euro6
print(rub10.name, rub10.amount)

# rub1 += 20
# print(rub1.name, rub1.amount)

# 20 + rub1
# print(rub1.name, rub1.amount)

# dol1 = DollarWallet("Дол", 10)

# rub1 + dol1
# print(rub1.name, rub1.amount)

# dol2 = DollarWallet("Дол", 2)
# rub2 = RubbleWallet("Руб", 60)

# dol2 + rub2
# print(dol2.name, dol2.amount)
# print(rub2.name, rub2.amount)

# rub2 += dol2
# print(rub2.name, rub2.amount)
# print(dol2.name, dol2.amount)

# dol2 += rub2
# print(dol2.name, dol2.amount)

# euro3 = EuroWallet("Евро", 1)
# rub3  = RubbleWallet("Руб", 10)
# dol3  = DollarWallet("Дол", 7)

# rub3 + euro3
# print(rub3.name, rub3.amount)

# rub3 += euro3
# print(rub3.name, rub3.amount)

# euro1 = EuroWallet("Евро", 1)
# euro1 + 1
# print(euro1.name, euro1.amount)

# 1 + euro1
# print(euro1.name, euro1.amount)

# euro1 += 1
# print(euro1.name, euro1.amount)

# rub4  = RubbleWallet("Руб", 70)
# euro2 = EuroWallet("Евро", 1)

# euro2 + rub4
# print(euro2.name, euro2.amount)

# euro2 += rub4
# print(euro2.name, euro2.amount)

# dol3 + euro3
# print(dol3.name, dol3.amount)

# print(sum1.name, sum1.amount)
# print(sum2.name, sum2.amount)


# print(rub1.amount)


    