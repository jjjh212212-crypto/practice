def com(num,start):
    global result
    if num == 2:
        if (path[0][0]-path[1][0]) * (path[0][1]-path[1][1]) < 0:
            result+=1
        return
    for i in range(start,N):
        path.append(arr[i])
        com(num+1,i+1)
        path.pop()
T=int(input())
for t in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    path=[]
    result=0
    com(0,0)
    print(f'#{t} {result}')
