import sys
sys.setrecursionlimit(10**6) 
def fib(n,l):
  
  if n==1:
    l[n]=n
    return 1
  elif n ==0:
    l[n]=n
    return 0
  if l[n]==0:
    l[n]=fib(n-1,l)+fib(n-2,l)
  return l[n]
n=int(input())
l=[0]*(n+1)   #for memoization
print(fib(n,l))
print(l)
