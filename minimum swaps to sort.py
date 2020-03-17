t=int(input())
for q in range(t):
    n=int(input())
    a=[]
    d={}
    j=0
    for w in input().split():
        w=int(w)
        a.append(w)
        d[w]=j
        j+=1
        
    s=sorted(a)
    c=0
    for i in range(n):
        if a[i]!=s[i]:
            x1=a[i]
            x2=s[i]
            y1=d[x2]
            a[i],a[y1]=a[y1],a[i]
            d[x2]=i
            d[x1]=y1
            c+=1
    print(c)
