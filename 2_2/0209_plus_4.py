for t in range(1,11):
    N,st=map(str,input().split())
    lst=list(st)
    N=int(N)
    while True:
        before=len(lst)
        for i in range(len(lst)-1):
            if lst[i]==lst[i+1]:
                lst.pop(i)
                lst.pop(i)
                break
        if before == len(lst):
            break
    print(f'#{t}',''.join(lst))