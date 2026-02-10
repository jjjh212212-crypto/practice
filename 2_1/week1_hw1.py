T=int(input())
for t in range(1,T+1):
    N=int(input())
    lst=list(map(int,input().split()))
    for i in range(N-1):
        for j in range(N-i-1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] =lst[j+1],lst[j]
    print(f'#{t}',*lst)