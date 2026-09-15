class_held=int(input("Number of classes held: "))
attend=int(input("Number of classes attended: "))
percent=attend/class_held*100
cause=input("You have any medical cause (y/n): ")
print("percentage of class attended:",percent,"%")
if percent<=75 and cause=='n':
 print("you are not allowed")
else:
 print("you are allowed")
