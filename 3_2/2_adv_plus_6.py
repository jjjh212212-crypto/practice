def com(num,start,mn):
    global result
    if result <= mn - B:
        return
    if num == k:
        check = mn - B
        if check >= 0:
            result=min(result,check)
        return
    for i in range(start,N):
        com(num+1,i+1,mn+lst[i])

T=int(input())
for t in range(1,T+1):
    N,B=map(int,input().split())
    lst=list(map(int,input().split()))
    lst.sort()
    path=[]
    result=10000*N
    for i in range(1,N+1):
        if sum(lst[N-i:]) >= B:
            k=i
            com(0,0,0)
    print(f'#{t} {result}')
        