def dfs(n):
    global count
    if n == G:
        count+=1
        return
    if n not in dic:
        return
    for i in dic[n]:
        if visit[i]:
            continue
        visit[i] = True
        dfs(i)
        visit[i] = False
        
T=int(input())
for t in range(1,T+1):
    N,E=map(int,input().split())
    lst=list(map(int,input().split()))
    S,G=map(int,input().split())
    dic={}
    for i in range(E):
        s=lst[2*i]
        e=lst[2*i+1]
        if s not in dic:
            dic[s] = [e]
        else:
            dic[s].append(e)
    count=0
    visit=[False]*(N+1)
    visit[S] = True
    dfs(S)
    print(f'#{t} {count}')