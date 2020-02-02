#longest common prefix:

t=int(input())
for i in range(t):
    n=int(input())
    l=[]
    mini=10101010
    for a in input().split():
        ll=len(a)
        mini=min(ll,mini)
        l.append(list(a))
    op=""
    for i in range(mini):
        temp=[]
        for j in range(n):
            if j==0:
                temp=l[j][i]
            else:
                if temp==l[j][i]:
                    pass
                else:
                    temp=[]
                    break
        if temp==[]:
            break
        else:
            op=op+temp[0]
    if op=="":
        print("-1")
    else:
        print(op)
        
