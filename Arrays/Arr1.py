arr=[1,5,3,7,2,8,4]
if len(arr)==1 or arr[len(arr)-1]>arr[len(arr)-1]:
 print("1")
else:
 for i in range(len(arr)-1):
  if i==0 and arr[i]>arr[i+1]:
   print("1")
   break
  if (arr[i]>arr[i+1]) and (arr[i]>arr[i-1]):
   print("1")
   break
 else:
  print("0")