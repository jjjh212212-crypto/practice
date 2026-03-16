# stack dfs 형식
N=int(input())
node_n=int(input())
node={}
for i in range(node_n):
    a,b=map(int,input().split())
    if a not in node:
        node[a]=[b]
    else:
        node[a].append(b)
    if b not in node:
        node[b]=[a]
    else:
        node[b].append(a)
visit=set()
stack=[1]
while stack:
    now=stack.pop()
    visit.add(now)
    if now in node:   # ** 1 혼자 있을때 예외 케이스 고려 **
        next=node[now]
    else:
        continue
    for i in next:
        if i not in visit and i not in stack:
            stack.append(i)

print(len(visit)-1)

# 재귀함수 dfs 형식

def dfs(now):
    if now in visit:
        return
    else:
        visit.append(now)
    if now in node:
        next = node[now]
    else:
        return
    for i in next:
        if i not in visit:
            dfs(i)

N=int(input())
node_n=int(input())
node={}
for i in range(node_n):
    a,b=map(int,input().split())
    if a not in node:
        node[a]=[b]
    else:
        node[a].append(b)
    if b not in node:
        node[b]=[a]
    else:
        node[b].append(a)
visit=[]
dfs(1)
print(len(visit)-1)