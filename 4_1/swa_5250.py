import heapq
def dijkstra():
    pq =[(0,0,0)]
    while pq:
        x,y,score = heapq.heappop(pq)
        if score > dist[y][x] and dist[y][x] > 0 and (x!=0 or y!=0):
            continue
        for i in range(4):
            ny=y+idy[i]
            nx=x+idx[i]
            if 0<=nx<N and 0<=ny<N:
                h = lst[ny][nx] - lst[y][x]
                if h < 0:
                    h=0
                nscore = score + 1 + h
                if dist[ny][nx] > 0 and dist[ny][nx] > nscore or dist[ny][nx] == 0:
                    dist[ny][nx] = nscore
                    heapq.heappush(pq, (nx, ny, dist[ny][nx]))
    return


T=int(input())
for t in range(1,T+1):
    N=int(input())
    lst=[list(map(int,input().split())) for _ in range(N)]
    dist=[[0]*N for _ in range(N)]
    idy=[1,0,-1,0]
    idx=[0,1,0,-1]
    result=0
    dijkstra()
    print(f'#{t} {dist[N-1][N-1]}')