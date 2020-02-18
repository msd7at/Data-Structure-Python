n=int(input())
a=[0]*n
f,r=0,0
def enqueue(x):
    global r
    global f
    if f==(r+1)%n:
        print("quueue is full")
    else:
        r=(r+1)%n
        a[r]=x
def dequeue():
    global f
    global r
    if f==r:
        print("empty")
    else:
        f=(f+1)%n
        a[f]=0
