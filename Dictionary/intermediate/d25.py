#Find the second-largest distinct value in a dictionary.

dict = {'a': 10, 'b': 60, 'c': 30, 'd': 50, 'e': 20}
d=list(dict.items())

distinct_values = list(set(dict.values()))

for i in range (len(d)):
    for j in range(i+1,len(d)):
        if d[i][1] < d[j][1]:
            d[i],d[j]=d[j],d[i]
print(d)
if len(d) >= 2:
    second_largest = d[1]
    print(f"Second-largest distinct value: {second_largest}")
else:
    print("No second-largest value")