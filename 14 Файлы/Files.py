"""

Напишите функцию get_popular_name_from_file(filename), 
которая считывает файл, в котором в каждой строке записаны имя и фамилия через пробел. 
filename - это имя файла, в котором записаны эти имена. 
Вам нужно вернуть строку - самое популярное имя в файле. 
Если таких имен несколько, 
они должны быть перечислены через запятую внутри строки в алфавитном порядке.

Формат ввода
Джо Байден
Владимир Добрый
Владимир Злой
Джо Буш
Илон Маск

Формат вывода
Владимир, Джо

"""

from collections import defaultdict

def get_popular_name_from_file(filename):
    
    name_amount = defaultdict(int)
    popular_names = list()
    tmp_amount = 0
    
    with open(filename, "r", encoding='utf-8') as myfile:
        for line in myfile:
            name_amount[line.split()[0]] += 1
    
    sort_name_amount = sorted(name_amount.items(), key = lambda para: para[1], reverse = True)
       
    for para in sort_name_amount:
        if(len(popular_names) == 0):
            popular_names.append(para[0])
            tmp_amount = para[1]
            continue
        if(tmp_amount > para[1]):
            break
        if(tmp_amount == para[1]):
            popular_names.append(para[0])
        
    sort_popular_names = sorted(popular_names)
    
    out_str =  ", ".join(sort_popular_names)
        
    
    return out_str
        
get_popular_name_from_file("names.txt")