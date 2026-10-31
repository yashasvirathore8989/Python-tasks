#Find all duplicate elements in a list and their frequencies.

numbers = [1,2,4,4,8,8]

freq = {}
for num in numbers:
    freq[num] = freq.get(num, 0) + 1
print("all frequencies:", freq)

for num, count in freq.items():
    if count > 1:
        print("duplicate items:",num)