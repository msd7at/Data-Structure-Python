t=int(input())
for q in range(t):
    n=int(input())
    l=[]
    m=0
    for i in input().split():
        i=int(i)
        m=max(i,m)
        l.append(i)
    x=[]
    a=[0]*(m+1)
    z=0
    for i in l:
        a[i]+=1
        z=max(z,a[i])
    for i in range(z+1):
      x.append([])
    for i in range(m+1):
     x[a[i]].append(i) 
    for i in range(z,0,-1):
      for d in x[i]:
        for j in range(i):
          print(d,end=" ")
    print()
"""
Given an array A[] of integers, sort the array according to frequency of elements. That is elements that have higher frequency come first. If frequencies of two elements are same, then smaller number comes first.

Input:
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows. The first line of each test case contains a single integer N denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output:
For each testcase, in a new line, print each sorted array in a seperate line. For each array its numbers should be seperated by space.

Constraints:
1 ≤ T ≤ 70
30 ≤ N ≤ 130
1 ≤ Ai ≤ 60 

Example:
Input:
2
5
5 5 4 6 4
5
9 9 9 2 5

Output:
4 4 5 5 6
9 9 9 2 5

Explanation:
Testcase1: The highest frequency here is 2. Both 5 and 4 have that frequency. Now since the frequencies are same then smaller element comes first. So 4 4 comes first then comes 5 5. Finally comes 6.
The output is 4 4 5 5 6.

Testcase2: The highest frequency here is 3. The element 9 has the highest frequency. So 9 9 9 comes first. Now both 2 and 5 have same frequency. So we print smaller element first.
THIS IS OUTPUT 9 9 9 2 5"""
