import sys
sys.stdin = open("sample_input.txt", "r")
# def com(num,start):
#     global result
#     if num == N-1:
#         mn=arr[0][0]
#         idx=0
#         idy=0
#         for i in used:
#             if i:
#                 idx += 1
#             else:
#                 idy += 1
#             mn+=arr[idx][idy]
#             if mn >= result:
#                 break
#         result=min(result,mn)
#         return
#     for i in range(start,(N-1)*2):
#         if used[i] == True:
#             continue
#         used[i] = True
#         com(num+1,i+1)
#         used[i] = False
        


T=int(input())
for t in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    dp=[[0]*N for _ in range(N)]
    dp[0][0]=arr[0][0]
    for i in range(1,N):
        dp[i][0]=dp[i-1][0]+arr[i][0]
    for i in range(1,N):
        dp[0][i]=dp[0][i-1]+arr[0][i]
    for i in range(1,N):
        for j in range(1,N):
            dp[i][j]=arr[i][j] + min(dp[i-1][j],dp[i][j-1])

    print(f'#{t} {dp[N-1][N-1]}')



