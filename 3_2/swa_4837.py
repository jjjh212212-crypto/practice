def com(num,start,sm):
    global count
    if K < sm:
        return
    if num == N:
        if K == sm:
            count+=1
        return
    for i in range(start,mx+1):
        com(num+1,i+1,sm+i)

T=int(input())
for t in range(1,T+1):
    N,K=map(int,input().split())
    count=0
    if K >= 12:
        mx = 12
    else:
        mx = K
    com(0,1,0)
    print(count)