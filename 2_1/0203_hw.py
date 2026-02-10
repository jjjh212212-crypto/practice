for test_case in range(1,11):
    n=int(input())
    lst=list(map(int,input().split()))
    # s=sum(lst)
    # a=0
    # b=99
    # if (sum//100)+1
    # for i in range(n):
    #     lst[b]=lst[b]-1
    #     lst[a]=lst[a]+1
    #     if lst[b-1]==lst[b]:
    for i in range(n):
        lst[lst.index(max(lst))]-=1
        lst[lst.index(min(lst))]+=1
        if max(lst)==min(lst):
            print(f'#{test_case} 0')
            break
    print(f'#{test_case} {max(lst)-min(lst)}')