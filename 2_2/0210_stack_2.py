import sys
sys.stdin = open("sample_input.txt", "r")
T=int(input())
for t in range(1,T+1):
    V,E=map(int,input().split())
    edge = [list(map(int,input().split())) for _ in range(E)]
    start,goal=map(int,input().split())
    edge_dic={}
    for i in edge:
        key = i[0]
        value = i[1]
        if key not in edge_dic:
            edge_dic[key]=[]
        edge_dic[key] += [value]
    stack=[]
    visit=[]
    while start!=goal:
        now=start
        if start not in stack:
            stack.append(start)
        if start not in visit:
            visit.append(start)
        if start not in edge_dic:
            stack.pop()
        ver = edge_dic[stack[-1]]
        for i in range(len(ver)):
            if ver[i] not in visit:
                start = ver[i]
                break
        if now == start:
            stack.pop()
            if stack ==[]:
                break
            else:
                start=stack[-1]
    if start == goal:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')