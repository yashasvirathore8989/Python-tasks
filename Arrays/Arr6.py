arr=[1,2,3,2,4,2,5,5,2]
target=2
count=0

for i in range(len(arr)):
 if arr[i]==target:
  count+=1
print("Count of",target,":",count)