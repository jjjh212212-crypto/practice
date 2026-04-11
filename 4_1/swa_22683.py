from collections import deque

def bfs(x,y,k,vector,count):
    que = deque()
    que.append((x,y,k,vector,count))
    visit=[[float('inf')]*N for _ in range(N)]
    visitk=[[K]*N for _ in range(N)]
    while que:
        dx,dy,dk,v,cnt = que.popleft()
        if visit[dy][dx] <= cnt and visitk[dy][dx] >= dk:
            continue
        visit[dy][dx] = cnt
        visitk[dy][dx] = dk
        for i in range(4):
            if abs(v - i) == 2 and (x1 != dx or y1 != dy):
                continue
            idx = dx + nx[i]
            idy = dy + ny[i]
            dcnt = cnt
            if 0 <= idx < N and 0 <= idy < N:
                if (v - i) % 2 != 0:
                    dcnt+=1
                elif (v - i) % 2 == 0 and v - i != 0:
                    dcnt+=2
                if arr[idy][idx] == 'G':
                    que.append((idx,idy,dk,i,dcnt+1))
                elif arr[idy][idx] == 'T' and dk > 0:
                    que.append((idx,idy,dk-1,i,dcnt+1))
                elif arr[idy][idx] == 'Y':
                    if visit[idy][idx] <= dcnt:
                        break
                    visit[idy][idx] = dcnt+1
                    break
    
    if visit[y2][x2] == float('inf'):
        return -1
    return visit[y2][x2] 


T=int(input())
for t in range(1,T+1):
    N,K = map(int,input().split())
    # G = 땅
    # T = 나무
    # X = 현재 위치
    # Y = 이동하고자 위치
    # v = {북:0,동:1,남:2,서:3}
    arr = [list(input()) for _ in range(N)]
    nx = [0,1,0,-1]
    ny = [-1,0,1,0]
    bx,by=False,False
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                x1=j
                y1=i
                bx=True
            elif arr[i][j] == 'Y':
                x2=j
                y2=i
                by=True
            if bx and by:
                break
        if bx and by:
            break
   
    print(f'#{t} {bfs(x1,y1,K,0,0)}')