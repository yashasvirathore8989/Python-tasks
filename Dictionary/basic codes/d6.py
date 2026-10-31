'''Remove a key from a dictionary using pop(). Handle the case where the
key does not exist.'''

d1={"name":"Anvi","age":20,"city":"Indore"}
remove_key=d1.pop("age",None)
if remove_key is not None:
    print("updated dictionary :",d1)
else:
    print("key not exist")


#Calculate the sum of all numeric values in a dictionary.
