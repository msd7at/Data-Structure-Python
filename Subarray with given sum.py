"""Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. The first line of each test case is N and S, where N is the size of array and S is the sum. The second line of each test case contains N space separated integers denoting the array elements.

Output:
For each testcase, in a new line, print the starting and ending positions(1 indexing) of first such occuring subarray from the left if sum equals to subarray, else print -1.

Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= Ai <= 1010

Example:
Input:
2
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10
Output:
2 4
1 5"""

t=int(input())
for i in range(t):
    n,su=map(int,input().split())
    x=list(map(int,input().split()))
    s=0
    c=0
    k=0
    while k<n:
        if s<su:
            s=s+x[k]
            k+=1
        while s>su and c <k:
            s=s-x[c]
            c+=1
        if s==su:
            print(c+1,k)
            break
    else:
        print("-1")
