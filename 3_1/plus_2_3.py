T=int(input())
for t in range(1,T+1):
    a,b=map(str,input().split())
    print(f'#{t} {len(a)-(len(b)-1)*a.count(b)}')