arr=[10,5,7,3,8,9]
k=3
for i in range(len(arr)-1):
 for j in range(i+1, len(arr)):
  if arr[i]>arr[j]:
   arr[i],arr[j]=arr[j],arr[i]
print("Sorted array:",arr)
kth_smallest=arr[k-1]
kth_largest=arr[len(arr)-k]
print("Kth smallest :",kth_smallest)
print("Kth largest :",kth_largest)