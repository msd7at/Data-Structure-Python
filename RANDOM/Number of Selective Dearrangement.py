n=int(input())
# def dagn1(n):
#     if n==1 or n==2:
#         return n-1
#     return (n-1)*(dagn1(n-2)+(dagn1(n-1)))
# print(dagn1(n))

def dagn2(n):
    l=[0]*(n+1)
    l[2]=1
    ans=0
    for i in range(3,n+1):
        l[i]=(i-1)*(l[i-1]+l[i-2])
    print(l[n])
dagn2(n)

def dagn3(n):
    if n==1 or n==2:
        return n-1
    a=0
    b=1
    for i in range(3,n+1):
        a,b=b,(i-1)*(a+b)
    print(b)
dagn3(n)