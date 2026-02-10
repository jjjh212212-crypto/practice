T=int(input())
for t in range(1,T+1):
    result=None
    N,M=map(int,input().split())
    arr=[list(input()) for _ in range(N)]
    for _ in range(2):
        for i in range(N):
            for j in range(N+1-M):
                count=0
                for k in range(M//2):
                    if arr[i][j+k] == arr[i][j+M-k-1]:
                        count+=1
                if M//2 == count:
                    result = ''.join(arr[i][j:j+M])
        arr=list(map(list,zip(*arr)))
        if result:
            print(f'#{t} {result}')
            break
                        