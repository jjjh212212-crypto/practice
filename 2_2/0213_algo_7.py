for t in range(1,11):
    n=int(input())
    lst=list(map(int,input().split()))
    while lst[-1]!=0:
        for i in range(1,6):
            lst[0]-=i
            a=lst.pop(0)
            if a <= 0:
                lst.append(0)
                break
            lst.append(a)
    print(f'#{t}',*lst)