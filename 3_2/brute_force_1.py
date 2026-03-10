def dfs(num):
    global result
    if num == n-1:
        check = [1]+path+[1]
        mn=0
        for i in range(n):
            mn += lst[check[i]-1][check[i+1]-1]
        result = min(result, mn) 
        return
    for i in range(n-1):
        if used[i] == True:
            continue
        used[i] = True
        path.append(i+2)
        dfs(num+1)
        path.pop()
        used[i] = False

    

T=int(input())
for t in range(1,T+1):
    n=int(input())
    path=[]
    used=[False for _ in range(n-1)]
    lst=[list(map(int,input().split())) for _ in range(n)]
    result=100*n*n
    dfs(0)
    print(f'#{t} {result}')