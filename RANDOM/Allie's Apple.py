n=int(input())
i=1
ans=0
while True:
    for j in range(i+1):
        x=i*10 +j
        ans=ans+(i+j)*4
    
    if ans>=n:
        print(i*8)
        break
    i+=1
