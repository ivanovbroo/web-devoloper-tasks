# На вход с клавиатуры подаются числа (по одному). 
# Нужно вывести на экран сумму всех четных чисел. 
# Ввод прекращается, если введена пустая строка (""). 
# При любой ситауации, когда не попадаются четные числа, 
# вывести на экран нужно 0 (например, 
# числа не были введены вообще или были введены только нечетные числа).

#Формат ввода
#1
#2
#3
#4
#5
#6
#7
#8

#Формат вывода
#20

# Примечания
# Ответ проверяется для целочисенного типа данных посимвольно. 
# Т.е., допустим, ответ 100 будет правильным, в то время как 100.0 выдаст ошибку, 
# поскольку он отличается от правильного на два символа .0

summ = 0

while True:
    a = input()
    if not a:
        break
    if int(a) % 2 == 0:
        summ += int(a)
        
print(summ)