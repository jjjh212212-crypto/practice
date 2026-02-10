for t in range(1,11):
    n=int(input())
    arr=[list(input()) for _ in range(8)]
    count=0
    for _ in range(2):
        for i in range(8):
            for j in range(8-n+1):
                count2=0
                for k in range(n//2):
                    if arr[i][j:j+n][k] != arr[i][j:j+n][n-k-1]:
                        break
                    else:
                        count+=1
                if count2==n//2:
                    count+=1
        arr = list(map(list,zip(*arr)))
        if n==1:
            break
    print(f'#{t} {count}')