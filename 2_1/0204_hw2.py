T=int(input())
for t in range(1,T+1):
    N,K=map(int,input().split())
    arr = [i for i in range(1,13)]
    n=len(arr)
    lst=[]
    for i in range(1<<n):
        x=[]
        for j in range(n):
            if i & (1<<j):
                x.append(arr[j])
        lst.append(x)
    count=0
    for i in lst:
        if len(i) == N and sum(i) == K:
            count+=1
    print(f'#{t} {count}')    
    
        