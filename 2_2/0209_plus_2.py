T=int(input())
for t in range(1,T+1):
    arr=[list(input()) for _ in range(5)]
    maxlen=len(arr[0])
    result=''
    for i in arr:
        if maxlen < len(i):
            maxlen=len(i)
    for i in range(maxlen):
        for j in arr:
            if len(j) > i:
                result+=j[i]
    print(f'#{t} {result}')