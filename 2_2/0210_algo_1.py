import sys
sys.stdin = open("input (1).txt", "r")
for _ in range(1,11):
    t,N = map(int,input().split())
    lst = list(map(int,input().split()))
    dic={}
    for i in range(N):
        key = lst[2*i]
        value = lst[2*i+1]
        if key not in dic:
            dic[key] = []
        dic[key]+=[value]
    now=0
    stack=[]
    visit=[]
    while now!=99:
        start=now
        if now not in visit:
            stack.append(now)
        if now not in visit: # visit 에 없으면 추가
            visit.append(now)
        if now not in dic: # dic의 key값이 없으면 pop
            stack.pop()
        ver = dic[stack[-1]]
        for i in range(len(ver)):
            if ver[i] not in visit:
                now = ver[i]
                break
        if now == start:
            stack.pop()
            if stack == []:
                break
            else:
                now = stack[-1]

    result=0
    if now==99:
        result=1
    print(f'#{t} {result}')
        