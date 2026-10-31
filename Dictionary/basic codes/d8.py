#Calculate the sum of all numeric values in a dictionary.

my_dict = {'a': 10, 'b': 20, 'c': 30}
sum = 0
for value in my_dict.values():
    sum+=value
print("sum of all numeric values is : ",sum)