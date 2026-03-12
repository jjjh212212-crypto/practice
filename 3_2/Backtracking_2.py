def bus_stop(start,cnt):
    global result
    if result <= cnt:
        return
    if start >= lst[0]:
        result = cnt
        return

    for j in range(1, lst[start]+1):
        bus_stop(start+j,cnt+1)

T=int(input())
for t in range(1,T+1):
    lst=list(map(int,input().split()))
    result=lst[0]
    bus_stop(1,0)
    print(f'#{t} {result-1}')