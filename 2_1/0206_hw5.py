T=int(input())
for t in range(1,T+1):
    a=set(input())
    b=list(input())
    dic={}
    max=0
    for i in a:
        dic[i] = 0
    for i in b:
        if i in a:
            dic[i]+=1
    for value in dic.values():
        if max < value:
            max=value
    print(f'#{t} {max}')