arr=[1,5,3,7,2,8,4]
min=arr[0]
max=arr[0]

for i in range(1, len(arr)):
 if arr[i]<min:
  min=arr[i]
 elif arr[i]>max:
  max=arr[i]
print(f"{max} and {min}")