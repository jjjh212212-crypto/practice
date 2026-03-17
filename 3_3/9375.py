T=int(input())
for _ in range(T):
    N=int(input())
    clothes={}
    for i in range(N):
        a,b=map(str,input().split())
        if b not in clothes:
            clothes[b]=[a]
        else:
            clothes[b].append(a)
    result=1
    for i in clothes:
        result*=len(clothes[i])+1
    print(result-1)