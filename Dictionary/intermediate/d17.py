#Count the frequency of each number in a list.

d=[1, 2, 2, 3, 1, 2]
frequency={}
for digit in d:
    if digit in frequency:
        frequency[digit]+=1
    else:
        frequency[digit]=1
print(frequency)
