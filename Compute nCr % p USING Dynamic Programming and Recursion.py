t=int(input())
def fact(n,r,l):
    if l[n][r] != -1:
        return l[n][r]
    else:
        if r==n or r==0:
            l[n][r]=1
            return 1
        elif r>n:
            l[n][r]=0
            return 0
        l[n][r]=(fact(n-1,r,l)+fact(n-1,r-1,l))%((10**9)+7)
        return l[n][r]
        
for q in range(t):
    l=[]
    n,r=map(int,input().split())
    for i in range(n+1):
        k=[]
        for j in range(r+1):
            k.append(-1)
        l.append(k)
    print(fact(n,r,l))
