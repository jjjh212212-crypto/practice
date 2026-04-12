def dfs(n,k):
    global result
    if n == N:
        result = n
        return
    count=0
    for i in dic[k]:
        if visit[i] == False:
            count+=1
    if count == 0:
        if result < n:
            result = n
        return

    for i in dic[k]:
        if visit[i]:
            continue
        visit[i] = True
        dfs(n+1,i)
        visit[i] = False
    

T=int(input())
for t in range(1,T+1):
    result = 0
    N,M=map(int,input().split())
    dic={}
    visit=[False]*(N+1)
    for i in range(N):
        dic[i+1] = []
    for i in range(M):
        x,y=map(int,input().split())
        dic[x].append(y)
        dic[y].append(x)
    for i in range(1,N+1):
        visit[i]=True
        dfs(1,i)
        visit[i]=False
    print(f'#{t} {result}')
    