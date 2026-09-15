class_held=int(input("Number of classes held: "))
attend=int(input("Number of classes attended: "))
percent=attend/class_held*100
print("percentage of class attended:",percent,"%")
if percent<75:
 print("you are not allowed")
else:
 print("you are allowed")
