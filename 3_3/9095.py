from math import factorial as fac
def com(n,m,r):
    return fac(n)//(fac(m)*fac(r)*fac(n-m-r))

T=int(input())
for _ in range(T):
    N=int(input())
    count=0
    n3=0
    while n3*3 <= N:
        n=N-(n3*2)
        c=0
        while n >= c+n3:
            count += com(n,c,n3)
            n-=1
            c+=1
        n3+=1
    print(count)
        
