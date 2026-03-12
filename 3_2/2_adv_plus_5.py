def checkmate(x,y):
    for i in visit:
        if (x,y) in i:
            visit.append([])
            return False
    visit_x=[]
    visit_x.append((x,y))
    for i in range(2):
        if i==0:
            idx = x+1
            idy = y-1
            while 0 <= idx <= N-1 and 0 <= idy <= N-1:
                visit_x.append((idx,idy))
                idx+=1
                idy-=1
        else:
            idx = x+1
            idy = y+1
            while 0 <= idx <= N-1 and 0 <= idy <= N-1:
                visit_x.append((idx,idy))
                idx+=1
                idy+=1
    visit.append(visit_x)
    return True
                

def permutation(num):
    global count
    global visit
    if num >= 1:
        if not checkmate(num-1,path[num-1]):
            return
    if num == N:
        count+=1
        return
    for i in range(N):
        if used[i]:
            continue
        used[i]=True
        path.append(i)
        permutation(num+1)
        path.pop()
        visit.pop()
        used[i]=False

T=int(input())
for t in range(1,T+1):
    N=int(input())
    path=[]
    used=[False]*N
    visit=[]
    count=0
    permutation(0)
    print(f'#{t} {count}')
