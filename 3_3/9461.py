T=int(input())
for _ in range(T):
    N=int(input())
    a=[0]*N
    for i in range(N):
        if i < 3:
            a[i]=1
        else:
            a[i]=a[i-3]+a[i-2]
    print(a[N-1])

