T=int(input())
for t in range(1,T+1):
    N=int(input())
    arr=[[1],[1,1]]
    for i in range(2,N):
        center=[]
        for j in range(i-1):
            center.append(arr[i-1][j]+arr[i-1][j+1])
        arr.append([1]+center+[1])
    if N==1:
        arr.pop()
    print(f'#{t}')
    for i in arr:
        print(*i)