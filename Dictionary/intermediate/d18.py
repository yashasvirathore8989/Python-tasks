#Find the first non-repeating character in a string using a dictionary

s = "aabbcc"
freq = {}
for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
found = False
for char in s:
    if freq[char] == 1:
        print("First non-repeating character is:",char)
        found= True
        break
if not found:
    print("No non repeating element found")