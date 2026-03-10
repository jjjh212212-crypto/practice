def pro(x,y,d1,d2):
    a=[0,0,0,0,0]
    j=0
    idy=y
    while j != d1+x:
        if j < x:
            a[0]+=sum(arr[j][:idy+1])
        else:
            a[0]+=sum(arr[j][:idy])
            idy-=1
        j+=1
    j=0
    idy=y
    while j != d2+x+1:
        if j < x:
            a[1]+=sum(arr[j][idy+1:])
        else:
            a[1]+=sum(arr[j][idy+1:])
            idy+=1
        j+=1
        if idy+1 == N:
            break
    j=x+d1
    idy=y
    while j != N:
        a[2]+=sum(arr[j][:idy-d1])
        if j < x+d1+d2:
            idy+=1
        j+=1
    j=x+d2+1
    idy=y
    while j != N:
        a[3]+=sum(arr[j][idy+d2:])
        if j <= x+d1+d2:
            idy-=1
        j+=1
    a[4]=sm-sum(a)
    return max(a)-min(a)

import itertools
N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
sm=0
for i in arr:
    sm+=sum(i)
mn=sm
for i in itertools.product(range(N),repeat=2):
    d1=i[0]
    d2=i[1]
    if d1+d2 >= N:
        continue
    x_x=[i for i in range(N-d1-d2)]
    y_y=[i for i in range(d1,N-d2)]
    for x in x_x:
        for y in y_y:
            result=pro(x,y,d1,d2)
            if mn >= result:
                mn = result
print(mn)


