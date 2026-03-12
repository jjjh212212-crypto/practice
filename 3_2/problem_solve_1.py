T=int(input())
for t in range(1,T+1):
    A,B,C=map(int,input().split())
    count=0
    while A>=1 and B>=2 and C>=3:
        if A<B<C:
            break
        while A >= min(B,C):
            A-=1
            count+=1
        while B >= C:
            B-=1
            count+=1
        
    if A<1 or B<2 or C<3:
        print(f'#{t} -1')
    else:
        print(f'#{t} {count}')
    