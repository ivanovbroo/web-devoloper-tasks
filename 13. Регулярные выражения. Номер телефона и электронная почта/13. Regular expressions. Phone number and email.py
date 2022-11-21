# Написать функцию, которая на вход принимает строку, 
# а на выход выдает булево значение (True или False), которое истинно, 
# если полученная строка соответствует российскому номеру телефона или адресу электронной почты.

# Сигнатура функции:

# check_string(string) -> bool

# Формат ввода
# +7-916-000-00-00

# Формат вывода
# True

# Примечания
# Допустимые форматы телефонов. Код страны - всегда либо 7, либо 8, либо +7, либо опущен; 
# код оператора может быть любой:

# 89160000000
# +79160000000
# 9160000000
# 8(916)000-00-00
# +7(916)000-00-00
# (916)000-00-00
# 8 (916) 000-00-00
# +7 (916) 000-00-00
# (916) 000-00-00
# 8(916)0000000
# +7(916)0000000
# (916)0000000
# 8-916-000-00-00
# +7-916-000-00-00
# 916-000-00-00

# Валидным адресом электронной почты будем считать строки, 
# содержащие @ и не меньше одной точки (после точки - не меньше двух символов), например:
# abc@abc.ab
# abc@abc.ab.ab
# a@ab.ab
# abc.abc@abc.abc

# Невалидные адреса:
# @abc.abc
# abc@abc
# abc@abc.a
# abc@abc.abc.a
# abc@abc.
# abc@abc@abc

import re

def formatting_number(string):
    line = re.sub(r'\+', r'', string)
    line = re.sub(r'-', r'', line)
    line = re.sub(r'\(', r'', line)
    line = re.sub(r'\)', r'', line)
    line = re.sub(r' ', r'', line)     
        
    return line

def check_string(string):
    # проверка строки, является ли номером
    if(string[0] == "+" or string[0] == "7" or 
       string[0] == "8" or string[0] == "(" or string[0] == "9"):
        
        # форматирование, убираем лишние символы
        line = formatting_number(string)
        
        pattern = re.compile(r'([78]|[9])([0-9]{10}$|[0-9]{9}$)')
        
        # записывать могут по разному номер и в соответствии с паттерном нужно не больше 10 цифр(на 9 номер)
        # не меньше 11 (на 7 или 8 номер)
        if(line[0] == "9" and len(line) > 10):
            return False 
        if((line[0] == "7" or line[0] == "8") and len(line) < 11):
            return False 
        # проверка нашего номера с помощью паттерна
        if pattern.match(line):
            return True
        else:
            return False 
    # проверка строки, является ли email
    elif(re.search(r'\@', string) != None):
        
        # проверка нет ли перед @ символы
        if(string[0] != '@'):
            raw_str = re.search(r'@', string)
            
            line =  string[raw_str.end():]     
            
            # если нет точки
            if(re.search(r'\.', line) == None):
                return False
            # после точки - не меньше двух символов
            if(re.search(r'\..{2,}', line) == None):
                return False
            # содержит после @ еще одну @
            if(re.search(r'\@', line) != None):
                return False
            # содержание точки/точек и сколько после них символов 
            if(re.findall(r'\.\w+', line) != None):
               list_dot = re.findall(r'\.\w+', line)
               for dot in list_dot:
                   # после точки - не меньше двух символов
                   if(len(dot) < 3):
                       return False
            
            return True
        
    return False

# правильные номера телефонов
number_list_test = ["+79160000010", "9160000000", "8(916)000-00-00", "+7(916)000-00-00",
                  "(916)000-00-00", "8 (916) 000-00-00", "+7 (916) 000-00-00",
                  "(916) 000-00-00", "8(916)0000000", "+7(916)0000000", "(916)0000000",
                  "8-916-000-00-00", "+7-916-000-00-00", "916-000-00-00"
                ]

for number in number_list_test:
    print(check_string(number))

# неправильные адреса
email_list_test = ["@abc.abc", "abc@abc", "abc@abc.a", "abc@abc.abc.a", "abc@abc.", "abc@abc@abc"]

for email in email_list_test:
    print(check_string(email))

print(check_string("abc@abc."))





















