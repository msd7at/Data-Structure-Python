t=int(input())
for q in range(t):
    l=[]
    n,r=map(int,input().split())
    for i in range(n+1):
        k=[]
        for j in range(r+1):
            k.append(0)
        l.append(k)
    for i in range(n+1):
        l[i][0]=1
    for i in range(r+1):
        l[0][j]=0
    for i in range(1,n+1):
        for j in range(1,r+1):
            l[i][j]= ((l[i-1][j-1]+l[i-1][j])%((10**9)+7))
    print(l[n][r])
    
