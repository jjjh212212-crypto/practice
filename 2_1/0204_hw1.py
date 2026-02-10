def block(a,b,c,d):
    block=set()
    for i in range(a,c+1):
        for j in range(b,d+1):
            block.add((i,j))
    return block

T=int(input())
for i in range(1,T+1):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    red=set()
    blue=set()
    for j in range(n):
        if arr[j][4] == 1:
            red = red | block(arr[j][0],arr[j][1],arr[j][2],arr[j][3])
        else:
            blue = blue | block(arr[j][0],arr[j][1],arr[j][2],arr[j][3])
    print(f'#{i} {len(red & blue)}')