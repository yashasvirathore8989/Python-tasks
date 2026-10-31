sentence = "Python is easy and Python is powerful"
words = sentence.lower()
words=sentence.split()
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
print("Frequency of words is :",frequency)