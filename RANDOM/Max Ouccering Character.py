s=input()
d1={}
for i in s:
    if i in d1:
        d1[i]+=1
    else:
        d1[i]=1
m=-100
ans=""
for i in d1:
    if m<d1[i]:
        m=d1[i]
        ans=i
c=0
k=0
for i in d1:
    if d1[i]==m:
        c+=1
    if c==2:
        print(0)
        k=1
if not k:
    print(ans)