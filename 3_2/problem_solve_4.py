import sys
sys.stdin = open("sample_input.txt", "r")
manhole_dict = {
    1: (1, 1, 1, 1), 
    2: (1, 1, 0, 0),
    3: (0, 0, 1, 1),
    4: (1, 0, 0, 1),
    5: (0, 1, 0, 1),
    6: (0, 1, 1, 0),
    7: (1, 0, 1, 0)
}

opp = {
    0:1,
    1:0,
    2:3,
    3:2
}

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(start_r,start_c,L):
    q = [(start_r,start_c,1)]
    visit = [[False]*M for _ in range(N)]
    visit[start_r][start_c] = True
    count=1

    while q:
        r,c,time = q.pop(0)

        if time == L:
            continue

        current_manhole = manhole_dict[arr[r][c]]
        for i in range(4):
            if current_manhole[i] == 1:
                nr = r + dr[i]
                nc = c + dc[i]
                if 0<=nr<N and 0<=nc<M and arr[nr][nc] != 0 and not visit[nr][nc]:
                    next_manhole = manhole_dict[arr[nr][nc]]

                    if next_manhole[opp[i]] == 1:
                        visit[nr][nc] = True
                        q.append((nr,nc,time+1))
                        count+=1
    return count

T=int(input())
for t in range(1,T+1):
    N,M,R,C,L=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    result=bfs(R,C,L)
    print(f'#{t} {result}')
        