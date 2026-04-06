import sys 
input = sys.stdin.readline
N,K=map(int,input().split())
lst=[]
for _ in range(N):
    lst.append(int(input().strip()))
start = 1
end = max(lst)
mid = ( start + end ) // 2
while start != mid and end != mid:
    count=0
    for j in lst:
        count += j // mid
        if count >= K:
            start = mid
            break
    if count < K:
        end = mid
    mid = ( start + end ) // 2
count = 0
for j in lst:
    count += j // (mid+1)
    if count == K:
        mid += 1
print(mid)