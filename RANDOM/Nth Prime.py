num=int(input())
n=100001
l=[True]*n
ans=[]
for i in range(2,(n//2)+1):
    if l[i]:
        ans.append(i)
        for j in range(i*i,n,i):
            l[j]=False
# print(ans)
print(ans[num-1])