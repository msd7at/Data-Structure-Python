graph=[]
n=int(input())
for i in range(n):
    graph.append(list(map(int,input().split())))
in_deg=[0]*n
out_deg=[0]*n
for i in range(n):
    ss=len(graph[i])
    in_deg[i]=ss
    for j in range(ss):
        aa=graph[i][j]
        out_deg[aa]+=1
print(in_deg)
print(out_deg)
