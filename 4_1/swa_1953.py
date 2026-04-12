from collections import deque
import sys
sys.stdin = open("sample_input (2).txt", "r")
def bfs():
    global result
    visit=[[0]*M for _ in range(N)]
    visit[R][C]=1
    que=deque()
    que.append((C,R,0))
    while que:
        x,y,count = que.popleft()
        for i in dic[arr[y][x]]:
            idx = x + nx[i]
            idy = y + ny[i]
            if 0<=idx<M and 0<=idy<N and arr[idy][idx] != 0:
                for j in dic[arr[idy][idx]]:
                    if abs(j-i) == 2 and visit[idy][idx] == 0 and count < L-1:
                        que.append((idx,idy,count+1))
                        visit[idy][idx]=1
                        result+=1

ny=[-1,0,1,0]
nx=[0,1,0,-1]
dic={
    1:[0,1,2,3],
    2:[0,2],
    3:[1,3],
    4:[0,1],
    5:[1,2],
    6:[2,3],
    7:[0,3]
}
T=int(input())
for t in range(1,T+1):
    N,M,R,C,L=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    result=1
    bfs()
    print(f'#{t} {result}')