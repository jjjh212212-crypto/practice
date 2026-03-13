T=int(input())
for _ in range(T):
    N=int(input())
    cnt0=0
    cnt1=1
    if N==0:
        print(1,0)
    else:
        for i in range(N-1):
            cnt1,cnt0 = cnt1+cnt0,cnt1
        print(cnt0,cnt1)