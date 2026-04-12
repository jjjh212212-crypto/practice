from collections import deque
import heapq

T=int(input())
for t in range(1,T+1):
    N=int(input())
    arr=[list(map(int,list(input()))) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                x1=j
                y1=i
            elif arr[i][j] == 3:
                x2=j
                y2=i
    nx=[0,1,0,-1]
    ny=[-1,0,1,0]
    que = []
    que.append((0,x1,y1,212))
    visit=[[float('inf')]*N for _ in range(N)]
    visit[y1][x1] = 0
    while que:
        score,dx,dy,dv = heapq.heappop(que)
        if dx == x2 and dy == y2:
            continue
        for i in range(4):
            if abs(dv - i) == 2:
                continue
            idx = dx + nx[i]
            idy = dy + ny[i]
            if 0<=idx<N and 0<=idy<N and arr[idy][idx] != 1 and visit[idy][idx] > score + 1:
                heapq.heappush(que,(score+1,idx,idy,i))
                visit[idy][idx] = score + 1
    if visit[y2][x2] == float('inf'):
        print(f'#{t} 0')
    else:        
        print(f'#{t} {visit[y2][x2]-1}')
        

