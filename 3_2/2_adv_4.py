def permutation(num,percent):
    global result
    if percent <= result:
        return
    if num == N:
        result=percent
        return
    for i in range(N):
        if used[i] or arr[len(path)][i] == 0 :
            continue
        used[i]=True
        path.append(i)
        permutation(num+1,percent*arr[len(path)-1][i])
        path.pop() 
        used[i]=False       
T=int(input())
for t in range(1,T+1):
    N=int(input())
    arr=[list(map(lambda x: int(x) / 100,input().split())) for _ in range(N)]
    path=[]
    used=[False]*N
    result=0
    permutation(0,1)
    print(f'#{t} {result*100:.6f}')