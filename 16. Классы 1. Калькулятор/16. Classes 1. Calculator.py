"""

Опишите класс Calculator, который будет реализовывать следующие методы и поля:

sum(self, a, b) - сложение чисел a и b

sub(self, a, b) - вычитание

mul(self, a, b) - умножение

div(self, a, b, mod=False) - деление. 
Если параметр mod == True, то метод должен возвращать остаток 
от деления вместо деления. 
По умолчанию mod=False.

history(self, n) - этот метод должен возвращать строку с операцией 
по ее номеру относительно текущего момента (1 - последняя, 2 - предпоследняя). 
Формат вывода: sum(5, 15) == 20

last - строка того же формата, что в предыдущем пункте, 
в которой содержится информация о последней операции 
по всем созданным объектам калькулятора. 
Т.е. это последняя операция последнего использованного объекта калькулятор. 
Если операций пока не было, то None.

clear(cls) - метод, который очищает last, т.е. присваивает ему значение None.

Формат вывода
При сохранении строк в history и last нужно выводить 
только один знак после запятой дробного числа.
При выполнении деления с mod сам параметр mod не нужно записывать в лог.

"""

class Calculator:
    
    last = None
    
    def __init__(self):
        self._hist = list()
        
    def sum(self, a, b):        
        result = a + b
        output = f"sum({a}, {b}) == {round(result, 1)}"
        Calculator.last = output
        self._hist.append(output)
        return result;
                
    def sub(self, a, b):
        result = a - b
        output = f"sub({a}, {b}) == {round(result, 1)}"
        Calculator.last = output
        self._hist.append(output)
        return result;
        
    def mul(self, a, b):
        result = a * b
        output = f"mul({a}, {b}) == {round(result, 1)}"
        Calculator.last = output
        self._hist.append(output)
        return result;
        
    def div(self, a, b, mod=False):
        if(mod == True):
            result = a % b
        else:
            result = a / b
            
        output = f"div({a}, {b}) == {round(result, 1)}"
        
        Calculator.last = output
        self._hist.append(output)
        return result;
        
    def history(self, n):
        try:
            return self._hist[-n]
        except IndexError:
            return None
        
    @classmethod  
    def clear(cls):
        cls.last = None
        
    # @classmethod
    # def _last_operation(cls, value):
    #     cls.last = value
        

c = Calculator()
b = Calculator()

# print(c.sum(1, 2))
# print(c.sub(3, 2))
c.clear()
print(c.mul(3, 5.23))
#print(c.last)
print(c.div(3, 2))
print(c.last)

# print(c.last)
# print(b.last)
# print(c.history(1))
# print(c.last)
# print(c.clear())
        
# print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'))
    













































