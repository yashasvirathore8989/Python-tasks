'''Merge two dictionaries. If a key exists in both dictionaries, use the
    value from the second dictionary.'''

d1 = {'a': 10, 'b': 20}
d2 = {'b': 50, 'd': 40}
merged = d1.copy()
for key, value in d2.items():
    merged[key] = value
print(merged)