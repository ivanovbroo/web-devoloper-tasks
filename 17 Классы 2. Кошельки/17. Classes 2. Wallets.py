class BaseWallet:

    def __init__(self, name, amount):
        self.name =  name
        self.amount = amount 

    def __add__(self, other):
        tmp = self._copy()
        if isinstance(other, BaseWallet):
            other = other.to_base() / self.exchange_rate
        tmp.amount = self.amount + other
        return tmp

    def __iadd__(self, other):
        if isinstance(other, BaseWallet):
            other = other.to_base() / self.exchange_rate
        self.amount = self.amount + other
        return self

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        tmp = self._copy()
        if isinstance(other, BaseWallet):
            other = other.to_base() / self.exchange_rate
        tmp.amount = self.amount - other
        return tmp

    def __isub__(self, other):
        if isinstance(other, BaseWallet):
            other = other.to_base() / self.exchange_rate
        self.amount -= other
        return self
    
    def __rsub__(self, other):
        return (self - other) * (-1)

    def __mul__(self, other):
        tmp = self._copy()
        if isinstance(other, BaseWallet):
            other = other.to_base() / self.exchange_rate
        tmp.amount = self.amount * other
        return tmp
    
    def __imul__(self, other):
        if isinstance(other, BaseWallet):
            other = other.to_base() / self.exchange_rate
        self.amount = self.amount * other
        return self

    def __rmul__(self, other):
        return self * other


    def __truediv__(self, other):
        tmp = self._copy()
        if isinstance(other, BaseWallet):
            other = other.to_base() / self.exchange_rate
        tmp.amount = self.amount / other
        return tmp

    def __itruediv__(self, other):
        if isinstance(other, BaseWallet):
            other = other.to_base() / self.exchange_rate
        self.amount = self.amount / other
        return self

    def to_base(self):
        convert = self.amount * self.exchange_rate
        return convert

    def __str__(self):
        return "{} {}".format(self.name, self.amount) 

    def __eq__(self, other):
        if isinstance(other, BaseWallet):
            if(type(self).__name__ == type(other).__name__) and (self.amount == other.amount):
                return True
        return False

    def spend_all(self):
        if(self.amount > 0):
            self.amount = 0
            return self

            
class RubbleWallet(BaseWallet):
    exchange_rate = 1

    def __init__(self, name, amount):
        super().__init__(name, amount)

    def _copy(self):
        return RubbleWallet(self.name, self.amount)

    def __str__(self):
        return "Rubble Wallet " + super().__str__()

class DollarWallet(BaseWallet):
    exchange_rate = 60

    def __init__(self, name, amount):
        super().__init__(name, amount)

    def _copy(self):
        return DollarWallet(self.name, self.amount)

    def __str__(self):
        return "Dollar Wallet " + super().__str__()

class EuroWallet(BaseWallet):
    exchange_rate = 70

    def __init__(self, name, amount):
        super().__init__(name, amount)

    def _copy(self):
        return EuroWallet(self.name, self.amount)

    def __str__(self):
        return "Euro Wallet " + super().__str__()

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

# проверка создания класса за счет _copy
print("\n_copy")
print(rub2)
print(dol2)
print(euro2)

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

# проверка создания класса за счет _copy
print("\n_copy")
print(rub3)
print(dol3)
print(euro3)

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

# проверка создания класса за счет _copy
print("\n_copy")
print(rub5)
print(dol5)
print(euro5)

# тест сложение классов __add__
print("\nтест сложение классов __add__")

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

dol7 = dol6 + rub6
print(dol7)

euro6 = EuroWallet("Евро6", 1)
rub10 = rub7 + euro6
print(rub10.name, rub10.amount)

euro7 = euro6 + rub7
print(euro7)

euro8 = euro6 + euro7
print(euro8)

dol8 = dol6 + dol7
print(dol8)

# тест сложение классов __iadd__
print("\nтест сложение классов __iadd__")

rub11 = RubbleWallet("Руб11", 10)
rub11 += rub6
print(rub11)

rub11 += dol6
print(rub11)

rub11 += euro6
print(rub11)

# тест вычитание классов __sub__
print("\nтест вычитание классов __sub__")

rub12 = RubbleWallet("Руб12", 12)
rub13 = rub12 - 2
print(rub13)

euro12 = EuroWallet("Евро12", 12)
euro13 = euro12 - 2
print(euro13)

dol12 = DollarWallet("Дол12", 12)
dol13 = dol12 - 2
print(dol13)

rub14 = rub6 - dol6
print(rub14)

dol14 = dol6 - rub6
print(dol14)

euro14 = euro6 - rub7
print(euro14)

euro15 = euro6 - dol6
print(euro15)

# тест вычитание классов __isub__
print("\nтест вычитание классов __isub__")

rub12 = RubbleWallet("Руб12", 12)
rub12 -= 2
print(rub13)

euro12 = EuroWallet("Евро12", 12)
euro12 -= 2
print(euro13)

dol12 = DollarWallet("Дол12", 12)
dol12 -= 2
print(dol13)

rub6 -= dol6
print(rub6)

rub6+=60
dol6 -= rub6
print(dol6)

euro6 -= rub7
print(euro6)

# тест вычитание классов __rsub__
print("\nтест вычитание классов __rsub__")

rub15 = RubbleWallet("Руб15", 60)
rub16 = 70 - rub15
print(rub16)

dol15 = DollarWallet("dol15", 5)
dol16 = 2 - dol15
print(dol16)

# тест умножение классов __mul__
print("\nтест умножение классов __mul__")

rub17 = rub15 * 5
print(rub17)

rub17 *= 3
print(rub17)

rub18 = rub15 * dol15
print(rub18)

dol17 = 5 * dol15
print(dol17)

# тест деление классов __truediv__
print("\nтест деление классов __truediv__")

rub19 = rub15 / 5
print(rub19)

dol18 = dol15 / rub15
print(dol18)

# тест деление классов __itruediv__
print("\nтест вычитание классов __itruediv__")

dol18 /= 5
print(dol18)

rub15 /= dol18
print(rub15)

# тест сравнение классов __eq__
print("\nтест сравнение классов __eq__")
rub20 = RubbleWallet("Руб20", 10)
rub21 = RubbleWallet("Руб21", 10)

print(rub20 == rub21)
print(rub20 == rub15)
print(rub20 == dol15)
print(rub20 == 20)

# тест spend_all()
print("\nтест spend_all()")

rub20.spend_all()
print(rub20)

rub22 = RubbleWallet("Руб22", -10)
print(rub22)
rub22.spend_all()
print(rub22)



