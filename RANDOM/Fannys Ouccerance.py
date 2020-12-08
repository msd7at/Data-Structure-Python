s=input()
n=input()
n=n.lower()
ans=""
for i in s:
    k=i
    i=i.lower()
    if i==n:
        pass
    else:
        ans+=k
print(ans)