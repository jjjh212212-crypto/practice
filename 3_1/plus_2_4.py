T=int(input())
for t in range(1,T+1):
    arr=[list(input()) for _ in range(5)]
    mx=len(max(arr,key=len))
    lst=[]
    print(mx)
    for i in range(mx):
        for j in range(5):
            if len(arr[j]) > i:
                lst.append(arr[j][i])
    print(f'#{t}',''.join(lst))