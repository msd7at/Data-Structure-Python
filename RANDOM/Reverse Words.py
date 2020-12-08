s=input()
n=len(s)-1
ans=""
res=""
while n>=0:
    if s[n]==" ":
        ans=ans+res+" "
        res=""
    else:
        res=s[n]+res
    n-=1
ans=ans+res
print(ans)