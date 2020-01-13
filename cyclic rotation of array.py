x=list(map(int,input().split()))
r=int(input())
r=r%len(x)
c=0
while c<len(x):
    print(x[r],end=" ")
    r=(r+1)%len(x)
    c=c+1    
    
