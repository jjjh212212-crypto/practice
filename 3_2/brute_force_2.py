import sys
sys.stdin = open("sample_input.txt", "r")
def com(num,start):
    global result
    if num == N-1:
        mn=0
        idx=0
        idy=0
        for i in range((N-1)*2):
            mn+=arr[idx][idy]
            if i in path:
                idx += 1
            else:
                idy += 1
        result=min(result,mn)
        return
    for i in range(start,(N-1)*2):
        if used[i] == True:
            continue
        used[i] = True
        path.append(i)
        com(num+1,i+1)
        path.pop()
        used[i] = False
        


T=int(input())
for t in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    path = []
    used = [False for _ in range((N-1)*2)]
    result = 10*N*N
    com(0,0)
    print(f'#{t} {result+arr[N-1][N-1]}')
