n=int(input())
def res(input1):
    xa=0
    s=0
    while input1 > xa:
        s+=1
        xa=xa+12*(s*s)
    return s*8
print(res(n))
    
