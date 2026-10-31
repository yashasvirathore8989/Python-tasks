'''Create a dictionary from two lists: one list contains keys and the
    other contains values. Do not use zip().'''

keys = ['a', 'b', 'c', 'd']
values = [10, 20, 30, 40]
dict = {}
for i in range(len(keys)):
    dict[keys[i]] = values[i]
print(dict)