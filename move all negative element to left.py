arr=[int (i) for i in input().split()]
j=0
for i in range(len(arr)):
    if arr[i]<0:
        arr[i],arr[j]=arr[j],arr[i]
        j+=1
print(arr)
