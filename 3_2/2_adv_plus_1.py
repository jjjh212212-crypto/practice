path=[]
def com(num,start):
    global result
    if num == N:
        if sum(path) == K:
            result+=1
        return
    for i in range(start,12):
        # if used[i] == True:
        #     continue
        # used[i]=True
        path.append(i+1)
        com(num+1,i+1)
        path.pop()
        # used[i]=False
T=int(input())
for t in range(1,T+1):
    N,K=map(int,input().split())
    result=0
    com(0,0)
    print(f'#{t} {result}')