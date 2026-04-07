def dfs_back(n,sm):
    global result
    if result <= sm and result > 0:
        return
    if n == N:
        result = sm
        return
    for i in dic[n]:
        dfs_back(i[0],sm+i[1])

T=int(input())
for t in range(1,T+1):
    N,M=map(int,input().split())
    lst=[list(map(int,input().split())) for _ in range(M)]
    dic={}
    for i in lst:
        if i[0] not in dic:
            dic[i[0]]=[(i[1],i[2])]
        else:
            dic[i[0]].append((i[1],i[2]))
    result=0
    dfs_back(0,0)
    print(f'#{t} {result}')