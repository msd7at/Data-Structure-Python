https://practice.geeksforgeeks.org/problems/maximum-width-of-tree/1# link : https://practice.geeksforgeeks.org/problems/maximum-width-of-tree/1
def getMaxWidth(root):
    ans=[]
    if not root:
        return 0
    l=[root]
    m=0
    while l:
        k=[]
        c=0
        for i in l:
            k.append(root.data)
            c=c+1
        m=max(m,c)
        ans.append(k)
        temp=l
        l=[]
        for i in temp:
            if i.left:
                l.append(i.left)
            if i.right:
                l.append(i.right)
    return m
            
            
        
