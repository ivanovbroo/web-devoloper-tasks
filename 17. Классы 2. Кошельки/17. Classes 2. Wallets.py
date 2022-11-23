class BaseWallet:

    def __init__(self, name, amount):
        self.name =  name
        self.amount = amount 

    def to_base(self):
        convert = self.amount * self.exchange_rate
        return convert


# rub1 = RubbleWallet("Руб", 10)
# print(rub1.name, rub1.amount)

# rub1 + 20
# print(rub1.name, rub1.amount)

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

euro3 = EuroWallet("Евро", 1)
rub3  = RubbleWallet("Руб", 10)
dol3  = DollarWallet("Дол", 7)

rub3 + euro3
print(rub3.name, rub3.amount)

rub3 += euro3
print(rub3.name, rub3.amount)

euro1 = EuroWallet("Евро", 1)
euro1 + 1
print(euro1.name, euro1.amount)

1 + euro1
print(euro1.name, euro1.amount)

euro1 += 1
print(euro1.name, euro1.amount)

rub4  = RubbleWallet("Руб", 70)
euro2 = EuroWallet("Евро", 1)

euro2 + rub4
print(euro2.name, euro2.amount)

euro2 += rub4
print(euro2.name, euro2.amount)

# dol3 + euro3
# print(dol3.name, dol3.amount)

# print(sum1.name, sum1.amount)
# print(sum2.name, sum2.amount)


# print(rub1.amount)


    