n=int(input())
count=0
while n%5!=0:
    n-=3
    count+=1
    if n < 0:
        break
if n < 0:
    print(-1)
else:
    count+=n//5
    print(count)