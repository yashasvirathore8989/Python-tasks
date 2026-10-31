#Count the frequency of each character in a string.

s = "Hello"
freq = {}
for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print(freq)