# Combine two dictionaries by adding the values of common keys.

dict1 = {'a': 10, 'b': 20}
dict2 = {'b': 5, 'c': 7}
result = {}
for key in dict1:
    result[key] = dict1[key]
for key in dict2:
    if key in result:
        result[key] += dict2[key]
    else:
        result[key] = dict2[key]
print(result)