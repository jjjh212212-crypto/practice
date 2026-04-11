def solve(v,x,y):
    for i in range(C):
        if command[i] == 'R':
            v = (v+1)%4
        elif command[i] == 'L':
            v = (v-1)%4
        elif command[i] == 'A':
            idx = x + nx[v]
            idy = y + ny[v]
            if 0<=idx<N and 0<=idy<N:
                if arr[idy][idx] == 'T':
                    continue
                else:
                    x = idx
                    y = idy
    if x2 == x and y2 == y:
        return 1
    return 0
            

from collections import deque

T=int(input())
for t in range(1,T+1):
    N=int(input())
    arr=[list(input()) for _ in range(N)]
    Q=int(input())
    answer=[]
    ny = [-1,0,1,0]
    nx = [0,1,0,-1]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                x1 = j
                y1 = i
            elif arr[i][j] == 'Y':
                x2 = j
                y2 = i


    for _ in range(Q):
        C,command = map(str,input().split())
        C = int(C)
        answer.append(solve(0,x1,y1))
    print(f'#{t}',*answer)

