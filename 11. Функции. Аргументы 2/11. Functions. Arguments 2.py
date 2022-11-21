# Вам нужно написать функцию lists_sum, которая принимает произвольное количество списков чисел, 
# и возвращает сумму всех этих чисел. 
# Предусмотрите дополнительный аргумент unique, 
# который по умолчанию равен False, но если в функцию подается unique=True, 
# то функция должна вернуть сумму всех уникальных чисел из всех списков. 
# Если поданы только пустые списки или списки чисел вообще не поданы в функцию, 
# то считать сумму чисел нулём.

# Формат ввода
# lists_sum([1, 1], [1], [1, 2, 3])
# lists_sum([1, 1, 1], [1, 1], unique=True)
# lists_sum([1, 1, 1], unique=False)

# Формат вывода
# lists_sum([1, 1], [1], [1, 2, 3]) == 9
# lists_sum([1, 1, 1], [1, 1], unique=True) == 1
# lists_sum([1, 1, 1], unique=False) == 3

# про functools.reduce https://www.geeksforgeeks.org/reduce-in-python/
# https://docs-python.ru/standart-library/modul-functools-python/funktsija-reduce-modulja-functools/

import functools

def lists_sum(*args, unique=False):
    if(args == ()):
        return 0
    
    tmp_list = functools.reduce(lambda a, b: a + b, args)
    
    if(unique):
        return sum(set(tmp_list))
    else:
        return sum(tmp_list)   
        
print(lists_sum([1, 1], [1], [1, 2, 3]))
print(lists_sum([1, 1, 1], [1, 1], unique=True))
print(lists_sum([1, 1, 1], unique=False))
print(lists_sum([], [], [], unique=False))
print(lists_sum())