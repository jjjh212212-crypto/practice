T=int(input())
for i in range(1,T+1):
    K,N,M = map(int,input().split())
    lst=list(map(int,input().split()))
    count=0
    start=0
    j=0
    while True:
        start2=start
        while lst[j]<=start+K:
            j+=1
            if j == M:
                break
        start=lst[j-1]
        count+=1
        if start2 == start:
            print(f'#{i} 0')
            break
        if N-start<=K:
            print(f'#{i} {count}')
            break

