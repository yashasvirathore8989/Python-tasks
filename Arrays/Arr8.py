arr=[1,2,3,7,5]
target=12
cs=0
left=0
right=0
while left<=right:
 cs=cs+arr[right]
 if cs==target:
  print(f"{left},{right}")
  break
 while cs>target and left<right:
  cs =cs-arr[left]
  left+=1
 if cs==target:
   print(f"{left},{right}")
   break
 right+=1