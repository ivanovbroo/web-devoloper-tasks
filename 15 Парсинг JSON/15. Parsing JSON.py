"""

Задачи, аналогичные этой, часто встречаются в реальной веб-разработке. 
Будем получать и отдавать JSONы. К вам поступают данные в виде json-строки, 
в которых содержится список людей. Для каждого человека описаны различные его параметры, 
но вам нужно посчитать просто средний возраст всех людей из списка. 
Напишите функцию mean_age(json_string), которая принимает json строку,
считает средний возраст людей из входных данных и возвращает новую json-строку в том формате, 
который указан ниже.

Формат ввода
[
    {
        "name": "Петр",
        "surname": "Петров",
        "patronymic": "Васильевич",
        "age": 23,
        "occupation": "ойтишнек"
    },
    {
        "name": "Василий",
        "surname": "Васильев",
        "patronymic": "Петрович",
        "age": 24,
        "occupation": "дворник"
    }
]
Формат вывода
{"mean_age": 23.5}

"""

from statistics import mean
import json

def mean_age(json_string):
    json_py = json.loads(json_string)
    mean_age_dict = dict()
    age_list = list()
    
    for i in range(len(json_py)):
        age_list.append(json_py[i]["age"])
        
    mean_age = mean(age_list)
        
    mean_age_dict["mean_age"] = mean_age    
    
    return json.dumps(mean_age_dict)
    
    
json_str = json.dumps([
                    {
                        "name": "Петр",
                        "surname": "Петров",
                        "patronymic": "Васильевич",
                        "age": 23,
                        "occupation": "ойтишнек"
                    },
                    {
                        "name": "Василий",
                        "surname": "Васильев",
                        "patronymic": "Петрович",
                        "age": 24,
                        "occupation": "дворник"
                    }
                ], ensure_ascii=False)

print(mean_age(json_str))