n=int(input())
tweet_names =[]
for i in range(n):
    tweet_names.append(input())
d={}
for i in tweet_names:
    l=len(i)
    i=i[0:l-11]
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
dd={}
for i in d:
    if d[i] in dd:
        dd[d[i]].append(i)
    else:
        dd[d[i]]=[i]
print(dd)
for i in sorted(dd.keys()):
    x=dd[i]
    x.sort()
    for j in x:
        print(j,i)
