N=int(input())
lst=list(map(int,input().split()))
lst.sort()
a1=0
sum=0
for i in lst:
    a1 += i
    sum += a1
print(sum)