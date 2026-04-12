import sys
sys.stdin = open("sample_input (3).txt", "r")
def dfs(now):
    global result
    x,y=now
    stack=[(x,y,arr[y][x],False,1,212)]
    while stack:
        dx,dy,now_h,chance,count,dv=stack.pop()  
        if result < count:
            result = count 
        for i in range(4):
            idx = dx + nx[i]
            idy = dy + ny[i]
            if 0 <= idx < N and 0<= idy < N and abs(dv-i) != 2: 
                for j in range(K+1):
                    next_h = arr[idy][idx]-j
                    if next_h < now_h:
                        if j == 0:
                            stack.append((idx,idy,next_h,chance or False,count+1,i))
                        elif j!=0 and not chance:
                            stack.append((idx,idy,next_h,True,count+1,i))
                        elif j!=0 and chance:
                            break
def dfs_recursive(dx,dy,now_h,chance,count):
    global result
    if result < count:
        result = count
    for i in range(4):
        idx = dx + nx[i]
        idy = dy + ny[i]
        if 0 <= idx < N and 0<= idy < N:
            if visit[idy][idx]:
                continue
            for j in range(K+1):
                next_h = arr[idy][idx]-j
                if next_h < now_h:
                    if j == 0:
                        visit[idy][idx] = 1
                        dfs_recursive(idx,idy,next_h,chance or False,count+1)
                        visit[idy][idx] = 0
                    elif j!=0 and not chance:
                        if visit[idy][idx]:
                            continue
                        visit[idy][idx] = 1 
                        dfs_recursive(idx,idy,next_h,True,count+1)
                        visit[idy][idx] = 0
                    elif j!=0 and chance:
                        break



ny=[-1,0,1,0]
nx=[0,1,0,-1]
T=int(input())
for t in range(1,T+1):
    result=0
    N,K=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    visit=[[0]*N for _ in range(N)]
    high=0
    for i in arr:
        if high < max(i):
            high = max(i)
    high_point=[]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == high:
                high_point.append((j,i))
    for i in high_point:
        x,y=i[0],i[1]
        visit[y][x] = 1
        dfs_recursive(x,y,arr[y][x],False,1)
        visit[y][x] = 0

    print(f'#{t} {result}')