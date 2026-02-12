def fac(n):
    k=1
    for i in range(2,n+1):
        k*=i
    if n==0:
        k=1
    return k
def com(n,k):
    return fac(n)//(fac(k)*fac(n-k))
T=int(input())
for t in range(1,T+1):
    n=int(input())
    count=0
    for i in range(n//20+1):
        count+=com(n//10-i,i)*2**i
    print(f'#{t} {count}')