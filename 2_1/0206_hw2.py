T=int(input())
for t in range(1,T+1):
    lst=list(input())
    count=0
    for i in range(len(lst)//2):
        if lst[i] == lst[len(lst)-i-1]:
            count+=1
    if len(lst)//2 == count:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')