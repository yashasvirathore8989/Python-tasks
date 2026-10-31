#Find the common keys between two dictionaries.

dict1 = {'a': 10, 'b': 20}
dict2 = {'b': 5, 'c': 7}
common=[]
for key in dict1:
    if key in dict2:
        common.append(key)
print(common)