from math import factorial as fac
def com(n,c):
    return fac(n)//(fac(c)*fac(n-c))
N=int(input())
n=N
c=0
count=0
while n >= c:
    count+=com(n,c)
    n-=1
    c+=1
print(count%10007)