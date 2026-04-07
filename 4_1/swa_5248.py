T=int(input())
for t in range(1,T+1):
    N,M=map(int,input().split())
    lst = list(map(int,input().split()))
    group = [[lst[0],lst[1]]]
    for i in range(1,M):
        m1=lst[2*i]
        m2=lst[2*i+1]
        c = [-1,-1]
        for j in range(len(group)):
            if m1 in group[j]:
                c[0]=j
            elif m2 in group[j]:
                c[1]=j
        if c.count(-1) == 0:
            if c[0] > c[1]:
                group[c[1]]+=group.pop(c[0])
            if c[0] < c[1]:
                group[c[0]]+=group.pop(c[1])
        elif c.count(-1) == 1:
            if c[0]!=-1:
                group[c[0]].append(m2)
            else:
                group[c[1]].append(m1)
        elif c.count(-1) == 2:
            group.append([m1,m2])
    print(group)
    print(f'#{t} {len(group)+N-len(set(lst))}')