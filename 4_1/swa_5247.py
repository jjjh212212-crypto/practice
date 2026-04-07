from collections import deque 
    
T=int(input())
for t in range(1,T+1):
    N,M=map(int,input().split())
    que=deque([])
    k = N
    n = 0
    visit=[0]*1000001
    visit[k] = 1
    while k != M:
        if k*2 <= 1000000 and visit[k+1] == 0:
            que.append((k+1,n+1))
            visit[k+1] = 1
        if k-1 > 0 and visit[k-1] == 0:
            que.append((k-1,n+1))
            visit[k-1] = 1
        if k*2 <= 1000000 and visit[k*2] == 0:
            que.append((k*2,n+1))
            visit[k*2] = 1
        if 0 < k-10 and visit[k-10] == 0:
            que.append((k-10,n+1))
            visit[k-10] = 1
        k,n = que.popleft()
    print(f'#{t} {n}')