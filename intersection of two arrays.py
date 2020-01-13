n=int(input())
N,M=input().split()
x=list(map(int,input().split()))
y=list(map(int,input().split()))
l=[]
x=set(x)
for i in x:
    if i in y:
        l.append(i)
print(l)
