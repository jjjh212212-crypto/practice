for i in range(1,11):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(100)]
    mx=[]
    for j in range(100):
        mx.append(sum(arr[j]))
    for j in range(100):
        col=0
        for k in range(100):
            col += arr[k][j]
        mx.append(col)
    mx.append(sum([arr[j][j] for j in range(100)]))
    mx.append(sum([arr[j][99-j] for j in range(100)]))
    print(f'#{i} {max(mx)}')