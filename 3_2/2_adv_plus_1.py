path=[]
used=[False for _ in range(12)]
def com(num,start):
    global result
    if num == N:
        if sum(path) == K:
            result+=1
            return
    for i in range(start,12):
        if used[i] == True:
            continue
        used[i]=True
        path.append(i+1)
        com(num+1,i+1)
        path.pop()
        used[i]=False
T=int(input())
for t in range(1,T+1):
    N,K=map(int,input().split())
    # mn=0
    # mx=0
    # for i in range(1,N+1):
    #     mn+=i
    # for i in range(12,12-N,-1):
    #     mx+=i
    # if mn <= K <= mx:
    #     a=1
    # else:
    #     a=0
    # print(f'#{t} {a}')
    result=0
    com(0,0)
    print(f'#{t} {result}')