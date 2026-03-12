def two(lstA,i):
    l=0
    r=len(lstA)-1
    m=(l+r)//2
    bools=True
    a=0
    b=0
    while i!=lstA[m]:
        if l==r:
            bools=False
            break
        if i > lstA[m]:
            if a==1:
                bools=False
                break
            l=m+1
            a=1
            b=0
        elif i < lstA[m]:
            if b==1:
                bools=False
                break
            r=m-1
            b=1
            a=0
        m=(l+r)//2
    return bools

T=int(input())
for t in range(1,T+1):
    N,M=map(int,input().split())
    lstA=list(map(int,input().split()))
    lstB=list(map(int,input().split()))
    count=0
    lstA.sort()
    for i in lstB:
        if two(lstA,i):
            count+=1
    print(f'#{t} {count}')
