s=input()
n=int(input())
k=1
ans=0
for i in range(1,len(s),2):
    ans=ans+int(s[i])
    if ans >= n:
        print(s[i-1])
        k=0
        break
if k:
    print(-1)