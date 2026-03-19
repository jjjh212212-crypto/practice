def dfs(v):
    if v in visit:
        return
    visit.append(v)
    if v not in dic:
        return
    for i in dic[v]:
        dfs(i)
    
def bfs(v):
    que=[v]
    while que:
        a=que.pop(0)
        visit.append(a)
        if a not in dic:
            continue
        for i in dic[a]:
            if i not in visit and i not in que:
                que.append(i)
    return
N,M,V=map(int,input().split())
dic={}
for i in range(M):
    a,b=map(int,input().split())
    if a not in dic:
        dic[a]=[b]
    else:
        dic[a].append(b)
    if b not in dic:
        dic[b]=[a]
    else:
        dic[b].append(a)
for i in dic:
    dic[i].sort()
visit=[]
dfs(V)
print(*visit)
visit=[]
bfs(V)    
print(*visit)