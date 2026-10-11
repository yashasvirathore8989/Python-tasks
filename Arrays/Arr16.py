#subarrays count with equal 0s and 1s
arr=[1,0,0,1,0,1,1]
count=0
subarrays=[]

for i in range(len(arr)):
 zeros=0
 ones=0
 for j in range(i,len(arr)):
  if arr[j]==0:
   zeros+=1
  else:
   ones+=1
  
  if zeros==ones:
   count+=1
   subarrays.append(arr[i:j+1])
print("Count:",count)
print("Subarrays:",subarrays)