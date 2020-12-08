n=input()
s=[]
k=0
for i in n:
    if i=="{":
        s.append(i)
    elif i=="}":
        if s==[]:
            print("Error")
            k=1
            break
        else:
            if s[-1]=="{":
                s.pop()
            else:
                s.append(i)
if s==[] and not k:
    print("correct")
elif not k:
    print("Error")
        