#Group a list of words according to their length.

words= ["cat", "apple", "dog", "mango"]
grouped={}

for word in words:
    length=len(word)
    if length not in grouped:
        grouped[length]=[]
    grouped[length].append(word)

print(grouped)