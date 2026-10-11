arr=[1,5,7,5,7,3,6,8]
found=None
for i in range(len(arr)-1):
 for j in range(i+1,len(arr)):
  if arr[i]==arr[j]:
   found=arr[i]
   break  
 if found is not None:
  print(found)
  break
else:
 print("Repeating element not found!") 