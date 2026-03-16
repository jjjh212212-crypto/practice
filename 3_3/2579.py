# import sys
# input=sys.stdin.readline
# def dfs(now,sm,count):
#     if visit[now][count-1] <= sm:
#         visit[now][count-1] = sm
#     else:
#         return
#     global result
#     if now == N:
#         if result < sm:
#             result = sm
#         return
#     elif now == N-1:
#         if count != 2:
#             sm += lst[N]
#             if result < sm:
#                 result = sm
#         return
#     if count != 2:
#         dfs(now+1,sm+lst[now+1],count+1)
#     dfs(now+2,sm+lst[now+2],1)
# N=int(input().strip())
# lst=[0]+[int(input().strip()) for _ in range(N)]
# visit=[[0,0] for i in range(N*2)]
# result=0
# dfs(0,0,0)
# print(result)

# 제미나이 ver
N = int(input())
lst = [0] * (N+1)
for i in range(1, N + 1):
    lst[i] = int(input())

dp = [0] * (N+1)
dp[1] = lst[1]
if N >= 2:
    dp[2] = lst[1] + lst[2]
if N >= 3:
    dp[3] = max(lst[1] + lst[3], lst[2] + lst[3])

for i in range(4, N + 1):
    # (2칸 전에서 왔을 때) vs (3칸 전에서 1칸 전을 거쳐서 왔을 때)
    dp[i] = max(dp[i-2] + lst[i], dp[i-3] + lst[i-1] + lst[i])

print(dp[N])
