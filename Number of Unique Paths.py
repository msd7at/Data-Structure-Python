t=int(input())
for q in range(t):
    n,m=map(int,input().split())
    s=[]
    for i in range(n):
        f=[]
        for j in range(m):
            f.append(0)
        s.append(f)
    for i in range(n):
        s[i][0]=1
    for i in range(m):
        s[0][i]=1
    for i in range(1,n):
        for j in range(1,m):
            s[i][j]=s[i-1][j]+s[i][j-1]
    print(s[n-1][m-1])
