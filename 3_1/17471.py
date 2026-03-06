import itertools
N=int(input())
lst=list(map(int,input().split()))
arr=[list(map(int,input().split())) for _ in range(N)]
a=[]
for i in range(N//2):
    a.extend(itertools.combinations(range(1,N+1),i+1))

result=[]
for j in a:
    lst1=[]
    lst2=[]
    for i in range(1,N+1):
        if i in j:
            lst1.append(i)
        else:
            lst2.append(i)
    lst1.sort()
    lst2.sort()
    bools=True
    for i in [lst1,lst2]:
        now=i[0]
        stack=[now]
        visit=[now]
        while visit != i:
            k=1
            before=now
            while stack:
                if arr[now-1][0] > 0:
                    if arr[now-1][k] in i and arr[now-1][k] not in stack and arr[now-1][k] not in visit:
                        stack.append(arr[now-1][k])
                    k+=1
                    if len(arr[now-1]) <= k:
                        break
                else:
                    break
            now=stack[-1]
            if before == now:
                while stack and stack[-1] in visit:
                    stack.pop()
                if not stack:
                    bools=False
                else:
                    now=stack[-1]
            if not bools:
                break
            visit.append(now)
            visit.sort()
        if not bools:
            break
    if bools:
        n=0
        m=0
        for i in lst1:
            n+=lst[i-1]
        for i in lst2:
            m+=lst[i-1]
        result.append(abs(n-m))
if result:
    print(min(result))
else:
    print(-1)
            
        
