s=input()
ans=1
i=1
while i<len(s):
    k=1
    if s[i]>s[i-1]:
        while i<len(s) and s[i-1]<s[i]:
            k+=1
            i+=1
            ans=max(ans,k)
    else:
        i+=1
print(ans)
    
        