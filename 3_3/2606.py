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
stack=[1]
while stack:
    now=stack.pop()
    visit.append(now)
    next=node[now]
    for i in next:
        if i not in visit and i not in stack:
            stack.append(i)


print(len(visit)-1)