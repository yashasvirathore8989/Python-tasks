#Given a list of integers, find the second-largest distinct element without using sort(), sorted(), or max().

arr=[12,45,7,45,30,22,30]
k=3
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
    else:
        i+=1
        j+=1
print("sorted array : ",arr)

second_largest=arr[len(arr)-k]
print("second largest is:",second_largest)


