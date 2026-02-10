T=int(input())
for t in range(1,T+1):
    N,M=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    max=0
    for j in range(N-M+1):
        for k in range(N-M+1):
            s=sum([arr[j+a][k+b] for a in range(M) for b in range(M)])
            if s > max :
                max=s
    print(f'#{t} {max}')
