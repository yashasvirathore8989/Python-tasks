#Find the key associated with the largest value in a dictionary.

dict = {'a': 10, 'b': 7, 'c': 30}
max_key = None
max_val = None
for key, value in dict.items():
    if max_val is None or value > max_val:
        max_val = value
        max_key = key
print(max_key,":" ,max_val)