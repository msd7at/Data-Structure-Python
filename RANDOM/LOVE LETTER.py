n=input()
n=n.split()
k=int(input())
ans=[]
for i in n:
    l=len(i)
    t=""
    for j in range(l):
        t+=i[(j+k)%l]
    ans.append(t)
jj=0
print(n)
print(ans)
for i in range(len(n)):
    if n[i]==ans[i]:
        jj+=1
print(jj)