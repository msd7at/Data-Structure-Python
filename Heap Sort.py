def heapify(arr, n, i):
    '''
    :param arr: original array
    :param n: size of original array
    :param i: subtree rooted at ith index
    :return: 
    '''
    lar=i
    l=2*i + 1
    r=2*i + 1 + 1
    
    while l<n and arr[lar]<arr[l]:
        lar=l
    while r<n and arr[lar]<arr[r]:
        lar=r
    if i!= lar:
        arr[i],arr[lar]=arr[lar],arr[i]
        heapify(arr,n,lar)
        
def buildHeap(arr,n):
    '''
    :param arr: given array
    :param n: size of array
    :return: None
    '''
    # code here
    for i in range(n//2 -1,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0) 

        
