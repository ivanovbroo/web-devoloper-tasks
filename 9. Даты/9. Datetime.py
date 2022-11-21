# С клавиатуры вводится дата в формате DD-MM-YYYY. 
# Нужно вывести дату начала недели, 
# к которой относится введенная дата (дата понедельника недели), в таком же формате.

# Формат ввода
# 22-09-2022

# Формат вывода
# 19-09-2022

# Примечания
# Если введен понедельник - нужно вывести его же.

import datetime

raw_date = input().replace("-", " ").split()

DD   = 0
MM   = 0
YYYY = 0

for i in raw_date:
    if(DD == 0):
        DD = int(i)
    elif(MM == 0):
        MM = int(i)
    else:
        YYYY = int(i)
        
my_date = datetime.date(YYYY, MM, DD)

monday_date = my_date - datetime.timedelta(days = my_date.weekday())

print(datetime.datetime.strftime(monday_date, "%d-%m-%Y"))