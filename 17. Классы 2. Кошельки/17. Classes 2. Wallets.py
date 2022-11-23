class BaseWallet:

    def __init__(self, name, amount):
        self.name =  name
        self.amount = amount 

    def __add__(self, other):
        self.amount = self.amount + int(other) 
        return self

    def __iadd__(self, other):
        self.amount += int(other)
        return self

    def __radd__(self, other):
        return self + other

class RubbleWallet(BaseWallet):
    _currency = "rub"
    exchange_rate = 1

    def __add__(self, other):
        if isinstance(other, BaseWallet):

            if(other._currency == "dol"):
                convert = other.amount * other.exchange_rate
                super(RubbleWallet, self).__add__(convert)

            if(other._currency == "euro"):
                convert = other.amount * other.exchange_rate
                super(RubbleWallet, self).__add__(convert)
        else:
            super(RubbleWallet, self).__add__(other)

    def __iadd__(self, other):
        if isinstance(other, BaseWallet):

            if(other._currency == "dol"):
                convert = other.amount * other.exchange_rate
                super(RubbleWallet, self).__iadd__(convert)
                return self

            if(other._currency == "euro"):
                convert = other.amount * other.exchange_rate
                super(RubbleWallet, self).__iadd__(convert)
                return self
        else:
            super(RubbleWallet, self).__iadd__(other)
            return self
    

class DollarWallet(BaseWallet):
    _currency = "dol"
    exchange_rate = 60

    def __add__(self, other):
        if isinstance(other, BaseWallet):

            if(other._currency == "rub"):
                convert = other.amount / self.exchange_rate
                super(DollarWallet, self).__add__(convert)

        else:
            super(DollarWallet, self).__add__(other)

    def __iadd__(self, other):
        if isinstance(other, BaseWallet):

            if(other._currency == "rub"):
                convert = other.amount / self.exchange_rate
                super(DollarWallet, self).__iadd__(convert)
                return self
        else:
            super(DollarWallet, self).__iadd__(other)
            return self

class EuroWallet(BaseWallet):
    _currency = "euro"
    exchange_rate = 70

    def __add__(self, other):
        if isinstance(other, BaseWallet):

            if(other._currency == "rub"):
                convert = other.amount / self.exchange_rate
                super(EuroWallet, self).__add__(convert)

        else:
            super(EuroWallet, self).__add__(other)

    def __iadd__(self, other):
        if isinstance(other, BaseWallet):

            if(other._currency == "rub"):
                convert = other.amount / self.exchange_rate
                super(EuroWallet, self).__iadd__(convert)
                return self
        else:
            super(EuroWallet, self).__iadd__(other)
            return self

    



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


    