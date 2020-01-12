S=int(input("enter the max size of queue"))
Q=[" "]*S
rear=front=-1
def enqueue(X):
    global rear
    global front
    if front == rear == -1:
        front=rear=0
        Q[rear]=X
    elif (rear+1)%S==front:
        print("QUEUE IS FULL")
    else:
        rear=(rear+1)%S
        Q[rear]=X
def dequeue():
    global rear
    global front
    if front ==rear== -1:
        print("QUEUE IS EMPTY")
    elif front==rear:
        front=rear=-1
    else:
        print("deleted element is ",Q[front])
        Q[front]=" "
        front=(front+1)%S
