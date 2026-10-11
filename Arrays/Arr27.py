P = [10, 20, 30, 40, 50]
val = int(input("Enter value to search: "))
found = False
for i in range(len(P)):
    if P[i] == val:
        found = True
        break
if found == True:
    print("element found")
else:
    print("element not found")