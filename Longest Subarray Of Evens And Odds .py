# link: https://practice.geeksforgeeks.org/problems/longest-subarray-of-evens-and-odds/1/?track=sp-arrays-and-searching&batchId=152
def maxEvenOdd(arr,n):
    m=0
    c=0
    for i in range(n-1):
        if (arr[i]+arr[i+1] )%2!=0:
            c+=1
            m=max(m,c)
        else:
            c=0
    return m+1
