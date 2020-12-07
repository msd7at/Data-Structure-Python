va=list(map(int,input().split()))
ch=input()
n=int(input())
p=0
ne=0
for i in range(n):
    if ch[i]=="P":
        p+=va[i]
    else:
        ne+=va[i]
print(va,ch,p,ne)
print(abs(n-p)*100)