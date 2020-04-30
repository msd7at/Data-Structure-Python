def lm(head):
    i=0
    while head:
        head=head.next
        i+=1
    return i
def rotateList(head, k):
    l=lm(head)
    if l==k:
        return head
    i=0
    cur=head
    q=head
    while i<k and cur:
        t=cur
        cur=cur.next
        i+=1
    t.next=None
    head=cur
    while head:
        if head.next==None:
            head.next=q
            return cur
        head=head.next
""" Rotate a Linked List
Given a singly linked list of size N. The task is to rotate the linked list counter-clockwise by k nodes, where k is a given positive integer smaller than or equal to length of the linked list.

Input:
The first line of input contains the number of testcases T. For each test case, the first line of input contains the length of a linked list and the next line contains linked list elements and the last line contains k, by which linked list is to be rotated.

Output:
For each test case, print the rotated linked list.

User Task:
The task is to complete the function rotate() which takes a head reference as the first argument and k as the second argument. The printing is done automatically by the driver code.

Constraints:
1 <= T <= 100
1 <= N <= 103
1 <= k <= 103

Example:
Input:
2
8
1 2 3 4 5 6 7 8
4
5
2 4 7 8 9
Output:
5 6 7 8 1 2 3 4
8 9 2 4 7

Explanation:
Testcase 1: After rotating the linked list by 4 elements (anti-clockwise), we reached to node 5, which is (k+1)th node from beginning, now becomes head and tail of the linked list is joined to the previous head.
Testcase 2: After rotating the linked list by 3 elements (anti-clockwise), we will get the resulting linked list as 8 9 2 4 7."""
