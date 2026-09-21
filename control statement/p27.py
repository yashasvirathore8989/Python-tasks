ascii_val=65
for i in range(1,5):
 for j in range(2*i-1):
  print(chr(ascii_val),end=" ")
  ascii_val+=1
 print()