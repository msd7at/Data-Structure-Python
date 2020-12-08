io=list(map(int,input().split()))
lo=list(map(int,input().split()))
n=int(input())
h=0
def gidf(io,start,end,val):
    
    for i in range(start,end+1):
        if io[i]==val:
            return i
    return -1
def getheight(io,lo,start,end,h,n):
    if start>end:
        return 0
    gid=gidf(io,start,end,lo[0])
    if gid==-1:
        return 0
    lec=gid-start
    ric=end-gid
    ll=[None for _ in range(lec)]
    rl=[None for _ in range(ric)]
    lh,rh,k=0,0,0
    
    for i in range(n):
        for j in range(start,gid):
            if lo[i]==io[j]:
                ll[k]=lo[i]
                k+=1
                break
    k=0
    for i in range(n):
        for j in range(gid+1,end+1):
            if lo[i]==io[j]:
                rl[k]=lo[i]
                k+=1
                break

    if lec>0:
        lh=getheight(io,ll,start,gid-1,h,lec)
    if ric>0:
        rh=getheight(io,rl,gid+1,end,h,ric)
    h=min(lh+1,rh+1)
    return h
print(getheight(io,lo,0,n-1,h,n))
    