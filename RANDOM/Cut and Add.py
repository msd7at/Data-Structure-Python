s=input()
m=int(input())
n=int(input())
t=s
l=len(s)
ans=0
while True:
    i=0
    j=l-1
    io=""
    while i<m:
        io=s[j]+io
        j-=1
        i+=1
    s=io+s[0:l-m]
    ans+=1
    print(s)
    if s==t:
        break
    i=0
    j=l-1
    io=""
    while i<n:
        io=s[j]+io
        j-=1
        i+=1
    s=io+s[0:l-n]
    ans+=1
    print(s)
    if s==t:
        break
print(ans)
        
        
        
    