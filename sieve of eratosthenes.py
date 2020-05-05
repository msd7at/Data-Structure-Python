#print all prime numbers upto n.
#sieve of eratosthenes
n=int(input())
prime=[]
for i in range(n+1):
  prime.append(True)
for i in range(2,int(n/2)+1):
  if prime[i] is True:
    for j in range(i**2,n+1,i):
      prime[j]=False
for i in range(2,n+1):
  if prime[i]==True:
    print(i,end=" ")
      
#time complexity
#algo->(O(N log(log N)))
#overall->(O(n))
