T=int(input())
for t in range(T):
    N,M=map(int,input().split())
    lst=[list(map(int,input().split())),[0]*N]
    lst[1][M] = 1
    b=0
    count=0
    while b!=1:
        a=lst[0].pop(0)
        b=lst[1].pop(0)
        if lst[0]==[]:
            count+=1
            break
        if a < max(lst[0]):
            lst[0].append(a)
            lst[1].append(b)
            b=0
        else:
            count+=1
    print(count)
    