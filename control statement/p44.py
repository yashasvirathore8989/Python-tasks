for i in range(5,0,-1):
 print(" "*(6-i),end=" ")
 for j in range(1,2*i):
  if i==j or j==1 or i==5:
   print(j,end=" ")
  else:
   print(" ",end=" ")
 print()