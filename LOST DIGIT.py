#You are given a list of n-1 integers and these integers are in the range of 1 to n. There are no duplicates in the list. One of the integers is missing in the list. Write an efficient code to find the missing integer.
n= int(input())
s=n*(n+1)
s=s/2
su=0
x=list(map(int,input().split()))
for i in range(n-1):
    su=su+x[i]
print("the lost didgit is",int(s-su))
