
def maxLen(n, lis):
    d={0:0}
    s=0
    maxi=0
    u=0
    for k in range(n):
        if lis[k]==0:
            s=s-1
        else:
            s=s+1
        try:
            d[s]
        except KeyError:
            d[s]=k+1
        else:
            u=(k+1)-d[s]
            if u >maxi:
                maxi=u
    return maxi
#{ 
#  Driver Code Starts
# Driver Program
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(maxLen(n, arr))
# Contributed by: Harshit Sidhwa

# } Driver Code Ends
