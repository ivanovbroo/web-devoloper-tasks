import re

class Field(dict):

    _key_set = set()
    
    def _convert(self, raw_key):
        key = str()
        tmp = int()
        for i in raw_key:
            if(type(i) == int):
                tmp = i
            elif(type(i) == str):
                try:
                    tmp = int(i)
                except ValueError:
                    key += i
            else:
                raise ValueError

            if(tmp != 0 and key != ""):
                key += str(tmp)
 
        pattern = re.compile(r'[A-Z][0-9]+$')

        if pattern.match(key.upper()):
            return key.upper()    
        else:
            raise ValueError
    

    def _check_type(self, raw_key):

        if(type(raw_key) == str):
            key = self._convert(raw_key)
            return key
        elif(type(raw_key) == tuple):
            key = self._convert(raw_key)
            return key
        elif(type(raw_key) == tuple and len(raw_key) > 2):
            raise TypeError
        elif(type(raw_key) == str and len(raw_key) < 2):
            raise TypeError
        else:
            raise TypeError
    
    def __getitem__(self, raw_key):

        key = self._check_type(raw_key)

        if key in self._key_set:
            return super(Field, self).__getitem__(key)
        else:
            return None

    def __setitem__(self, raw_key, value):

        key = self._check_type(raw_key) 
        Field._key_set.add(key)    
        
        return super(Field, self).__setitem__(key, value)

    def __missing__(self, key):
        return None

    def __delitem__(self, raw_key):
        key = self._check_type(raw_key)
        Field._key_set.remove(key)
        super(Field, self).__delitem__(key)

    def __contains__(self, raw_key):
        
        key = self._check_type(raw_key)
        if key in Field._key_set:
            return True
        return False   

    def __iter__(self):
        return iter(self.values())

    def __getattr__(self, raw_key):
        try:
            return self[raw_key]
        except ValueError:
            return super(Field, self).__getattr__(raw_key)

    def __setattr__(self, raw_key, value): 
        try:
            self[raw_key] = value
        except ValueError:
            return super(Field, self).__setattr__(raw_key, value)

    def __delattr__(self, raw_key):

        try:
            self.__delitem__(raw_key)
        except ValueError:
            return super(Field, self).__delattr__(raw_key)

        

        

        

        
        



field = Field()  

field.g25 = 25
print(field["g25"])


print(field.__dict__)
print(field.g25)
del field.G25
print(field.g25)

field_test = Field()
field_test.abcde = 125
print(field_test.abcde, field_test.__dict__['abcde'] == 125)

del field_test.abcde
print(field_test.abcde, field_test.__dict__['abcde'] == 125)


# правильные ключи
field[1, 'a']   = 1
field['b', 1]   = 2
field['c', '1'] = 3
field['1', 'd'] = 4
field['1f']     = 5
field['g1']     = 6
field[1, 'K']   = 7
field['L', 1]   = 8
field['M', '1'] = 9
field['1', 'N'] = 10
field['1X']     = 11
field['Z1']     = 12

print(field["A1"])
print(field["B1"])
print(field["C1"])
print(field["D1"])
print(field["F1"])
print(field["G1"])
print(field["K1"])
print(field["L1"])
print(field["M1"])
print(field["N1"])
print(field["X1"])
print(field["Z1"])

# неправильные ключи
# field[1, 'aa']    = 1
# field['b', 1.5]   = 2
# field['c', '-6']  = 3
# field['A']        = 4
# field['27']       = 5
# field['GG']       = 6
# field['1.5', 'K'] = 7
# field[[1], 'K']   = 8

# print(field["H1"])

# del(field["A1"])
# # del(field["H1"])

# print("B1" in field)
# print(('D', '4') in field)

# for i in field:
#     print(i)

# print(field["C1"] is None)
