t=int(input())
for q in range(t):
    n=int(input())
    l=[0 for i in range(n+1)]
    l[0]=1
    for i in range(3,n+1):
        l[i]=l[i]+l[i-3]
    for i in range(5,n+1):
        l[i]=l[i]+l[i-5]
    for i in range(10,n+1):
        l[i]=l[i]+l[i-10]
    print(l[n])
    
"""
Consider a game where a player can score 3 or 5 or 10 points in a move. Given a total score n, find number of distinct combinations to reach the given score.

Input:
The first line of input contains an integer T denoting the number of test cases. T testcases follow.The first line of each test case is n.

Output:
For each testcase, in a new line, print number of ways/combinations to reach the given score.

Constraints:
1 ≤ T ≤ 100
1 ≤ n ≤ 1000

Example:
Input:
3
8
20
13

Output:
1
4
2

Explanation
For 1st example when n = 8
{ 3, 5 } and {5, 3} are the two possible permutations but these represent the same cobmination. Hence output is 1.
 
"""
