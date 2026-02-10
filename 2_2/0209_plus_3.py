T=int(input())
for t in range(1,T+1):
    a,b=map(str,input().split())
    print(f'#{t}',len(a)-a.count(b)*(len(b)-1))