for i in range(5,0,-1):
 for j in range(1,2*i):
  print(" "*(j-i),end=" ")
  if i==j or j==1 or j==5:
   print(j,end=" ")
  else:
   print("+",end=" ")
 print()