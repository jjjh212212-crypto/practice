n=int(input())
for i in range(1,n+1):
    a=[int(i) for i in str(input())]
    a.sort()
    count=0
    for j in range(4):
        for k in range(j+1,5):
            for h in range(k+1,6):
                if a[j]+2==a[k]+1==a[h]:
                    a[j]+=100
                    a[k]+=100
                    a[h]+=100
    a.sort()
    for j in range(4):
        if a[j]==a[j+1]==a[j+2]:
            a[j]+=100
            a[j+1]+=100
            a[j+2]+=100   
    if sum(a)>600:
        print(f'#{i} 1')
    else:
        print(f'#{i} 0')

        
