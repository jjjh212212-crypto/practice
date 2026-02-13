import sys
input=sys.stdin.readline
n=int(input())
lst=[]
a1=0
cnt=[0]*8001
k=[]
for i in range(n):
    m=int(input().strip())
    a1+=m
    k.append(m)
    cnt[m+4000]+=1
k.sort()
if a1<0:
    print(int(a1/n-0.5))
else:
    print(int(a1/n+0.5))
print(k[n//2])
mx=max(cnt)
if cnt.count(mx)>1:
    cnt[cnt.index(mx)]=0
print(cnt.index(mx)-4000)
print(k[-1]-k[0])
# while k < n//2+1:
#     k+=count[i]
#     if k >= n//2+1:
#         break
#     i+=1
# print(i-4000)
# if count.count(max(count))>1:
#     count[count.index(max(count))]=0
# print(count.index(max(count))-4000)
# print(mx-mn)


