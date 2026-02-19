n=int(input())
k=1
j=n-1
for i in range(2*n-1):
    print(' '*j+'*'*k)
    if i < n-1:
        k+=2
        j-=1
    else:
        k-=2
        j+=1