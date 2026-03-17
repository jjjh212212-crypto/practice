# 내 풀이
from math import sqrt
def mx_pro():
    for i in range(int_n,int(sqrt(n/cnt))-1,-1):
        pro(1,1,i**2)
        if bools ==True:
            break
    return bools
def pro(num,start,count):
    global bools
    if bools:
        return
    if num == cnt:
        if count == n:
            bools=True
        return 
    for i in range(start,int(sqrt(count))+1):
        c = count + i**2
        if c > n:
            break
        else:
            pro(num+1,i,c)

n=int(input())
int_n=int(sqrt(n))
mx = int_n ** 2
bools=False
for i in range(1,5):
    cnt=i
    mx_pro()
    if bools:
        result=i
        break
print(result)

# 제미나이 ver (DP)
n = int(input())

# 1. DP 테이블 초기화
# dp[i]는 최악의 경우 1의 제곱으로만 이루어져 있으므로 i개입니다.
# (예: 5 = 1^2 + 1^2 + 1^2 + 1^2 + 1^2 -> 5개)
dp = [i for i in range(n + 1)]

# 2. 1부터 n까지 작은 숫자부터 차례대로 정답을 채워나감 (Bottom-Up)
for i in range(1, n + 1):
    # i보다 작거나 같은 모든 제곱수(j*j)를 빼보면서 최솟값 갱신
    for j in range(1, int(i**0.5) + 1):
        dp[i] = min(dp[i], dp[i - j*j] + 1)

print(dp[n])