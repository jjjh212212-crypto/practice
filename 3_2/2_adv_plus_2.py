import sys
sys.stdin = open("sample_input (1).txt", "r")
def com(num,start):
    global result
    if num == N//2:
        a1=0
        a2=0
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if used[i] and used[j]:
                    a1+=arr[i][j]
                elif not used[i] and not used[j]:
                    a2+=arr[i][j]
        result=min(result,abs(a1-a2))
    for i in range(start,N):
        if used[i] == True:
            continue
        used[i] = True
        com(num+1,i+1)
        used[i] = False
    
T=int(input())
for t in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    used=[False] * N
    result = 20000 * N * N
    used[0]=True
    com(1,1)
    print(f'#{t} {result}')