arr = [4, 2, 7, 11, 5, 8]
x = 6
greater = None
lesser = None
for num in arr:
    if num > x:
        if greater == None or num < greater:
            greater = num
    if num < x:
        if lesser == None or num > lesser:
            lesser = num
print("Nearest greater than", x, "is", greater) 
print("Nearest lesser than", x, "is", lesser) 