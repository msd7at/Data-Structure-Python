n=int(input())
mat=[[int(i) for i in input().split()] for j in range(n)]

'''
let  _ 
    |  ==up left
    _| ==right down
    \ dg1
    and / dg2
'''
s=0
#upleft

for i in range(n):
    j=0
    if i==0:
        s=s+mat[i][i]
    else:
        s=s+mat[i][j]
        s=s+mat[j][i]
#for right down
for i in range(1,n):
    j=n-1
    if i==n-1:
        s=s+mat[i][i]
    else:
        s=s+mat[i][j]
        s=s+mat[j][i]
#dg1
for i in range(1,n-1):
    s=s+mat[i][i]
#dg2
for j in range(1,n-1):
    i=n-1-j
    if i!=j:
        s=s+mat[i][j]
print(s)
