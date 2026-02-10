T=int(input())
for t in range(1,T+1):
    lst=list(input())
    while True:
        n=len(lst)
        for i in range(len(lst)-1):
            if lst[i]==lst[i+1]:
                lst.pop(i)
                lst.pop(i)
                break
        if n == len(lst):
            break
    print(f'#{t} {len(lst)}')
            

