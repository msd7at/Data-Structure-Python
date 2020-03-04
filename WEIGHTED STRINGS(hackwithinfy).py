"""
In Hackerland every character has a weight. The weight of an English uppercase alphabet A-Z is given below :

A = 1

B = 2*A + A

C = 3*B + B

D = 4*C + C

….

Z = 26*Y + Y

The weight made up of these characters is the summation of weights of each character. Given a total string weight,
determine shortest string of given weight. If there is more than one solution, return the lexicographically smallest 
of them. For example, given weight = 25, and the weights of the first few characters of the alphabets are
A=1, B=3, C=12, D=60 
it is certain that no letter larger than C is required. 
Some of the strings with a total weight equal to the target are ABBBBC, ACC, AAAAAAABBBBBB. The shortest of these is ACC.
While any permutation of these characters will have same weight, this is the lexicographically smallest of them
"""
d={"A":1}
for i in range(2,27):
    val=64+i
    t=chr(val)
    t1=i*d[chr(val-1)]+d[chr(val-1)]
    d[t]=t1
s=int(input())
i="A"
while i in d and d[i]<=s:
    i=chr(ord(i)+1)
i=chr(ord(i)-1)
print(i)
l=[]
while s>0 and i>="A":
    if d[i]<=s:
        s=s-d[i]
        l.append(i)
    else:
        i=chr(ord(i)-1)
print(*l[::-1],sep="")
