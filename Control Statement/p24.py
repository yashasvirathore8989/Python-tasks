ascii_val=96
for i in range(1,5+1):
 for j in range(1,i+1):
  ascii_val+=1
  if i==j or j==1 or i==5:
   print(chr(ascii_val),end=" ")
  else:
   print(" ",end=" ")
 print()