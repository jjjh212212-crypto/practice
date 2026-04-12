from collections import deque

def bfs():
    que=deque()
    que.append((0,0,1,0))
    visit=[[float('inf')]*N for _ in range(N)]
    visit[0][0] = 0
    while que:
        dx,dy,dv,ds = que.popleft()
        for i in range(4):
            if abs(dv-i) == 2:
                continue
            idx = dx + nx[i]
            idy = dy + ny[i]
            if 0<=idx<N and 0<=idy<N:
                plus = arr[idy][idx] - arr[dy][dx]
                if plus < 0:
                    plus = 0
                nscore = ds+plus+1
                if nscore < visit[idy][idx]:
                    visit[idy][idx] = nscore
                    que.append((idx,idy,i,nscore))

    return visit[N-1][N-1]


ny=[-1,0,1,0]
nx=[0,1,0,-1]
T=int(input())
for t in range(1,T+1):
    N=int(input())
    arr= [list(map(int,input().split())) for _ in range(N)]
    print(f'#{t} {bfs()}')