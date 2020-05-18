import sys
sys.setrecursionlimit(150000)
def mci(i,j):
    if i<0 or i>len(a)-1 or j<0 or j>len(a[0])-1 or a[i][j]==0:
        return 
    a[i][j]=0
    mci(i-1,j-1)
    mci(i-1,j)
    mci(i-1,j+1)
    mci(i,j-1)
    mci(i,j+1)
    mci(i+1,j-1)
    mci(i+1,j)
    mci(i+1,j+1)
def findIslands(a,n,m):
    c=0
    for i in range(n):
        for j in range(m):
            if a[i][j]==1:
                mci(i,j)
                c+=1
    return c
"""
A group of connected 1's forms an island. The task is to complete the method findIslands() which returns the number of islands present. The function takes three arguments the first is the boolean matrix A and then the next two arguments are N and M denoting the size(N*M) of the matrix A .

Input:
The first line of input will be the number of testcases T, then T test cases follow. The first line of each testcase contains two space separated integers N and M. Then in the next line are the NxM inputs of the matrix A separated by space .

Output:
For each testcase in a new line, print the number of islands present.

User Task:
Since this is a functional problem you don't have to worry about input, you just have to complete the function findIslands().

Constraints:
1 <= T <= 100
1 <= N, M <= 100
0 <= A[i][j] <= 1

Example(To be used only for expected output) :
Input
2
3 3
1 1 0 0 0 1 1 0 1
4 4
1 1 0 0 0 0 1 0 0 0 0 1 0 1 0 0

Output
2
2

Explanation:
Testcase 1: The graph will look like
1 1 0
0 0 1
1 0 1
Here, two islands will be formed
First island will be formed by elements {A[0][0] ,  A[0][1], A[1][2], A[2][2]}
Second island will be formed by {A[2][0]}."""
