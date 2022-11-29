
def sort_listdict_for_dict(raw_dict):
    sort_dict = {}
    
    for i in raw_dict:
        tmp_name = ""
        for key, value in i.items():
            if(key == "name"):
                if(sort_dict.get(value) == None):
                    sort_dict[value] = 0
                tmp_name = value
            if(key == "amount"):
                sort_dict[tmp_name] += value
    
    return sort_dict
    

def get_balance(name, transactions):
    name_amount_dict = sort_listdict_for_dict(transactions)
    
    for key, value in name_amount_dict.items():
        if(key == name):
            return value       
    
    return 0


def count_debts(names, amount, transactions):
    name_amount_dict = sort_listdict_for_dict(transactions)
    party_dict = {} 
    
    for name in names:
        if(name_amount_dict.get(name) == None):
            party_dict[name] = amount
            continue
        if(name_amount_dict.get(name) >= amount):
            party_dict[name] = 0
            continue
        if(name_amount_dict.get(name) < amount):
            party_dict[name] = amount - name_amount_dict.get(name) 
            continue
            
    return party_dict

transactions = [
                {"name": "Василий", "amount": 500}, 
                {"name": "Петя", "amount": 100}, 
                {"name": "Василий", "amount": -300},
                {"name": "Никита", "amount": 0},
                {"name": "Гена", "amount": -500}
               ]

# print(get_balance("Василий", transactions))
# print(get_balance("Никита", transactions))
# print(get_balance("Петя", transactions))

print(count_debts(["Василий", "Петя", "Вова", "Никита", "Гена"], 150, transactions)) # == {"Василий": 0, "Петя": 50, "Вова": 150}