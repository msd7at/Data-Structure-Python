s=input()
n=input()
d1={}
d2={}
for i in s:
    i=i.lower()
    if i in d1:
        d1[i]+=1
    else:
        d1[i]=1
for i in n:
    i=i.lower()
    if i in d2:
        d2[i]+=1
    else:
        d2[i]=1
        
if d1==d2:
    print("yes")
else:
    print("no")
        
        