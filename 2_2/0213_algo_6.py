import sys
sys.stdin = open("input (6).txt", "r")
for t in range(1,11):
    N=int(input())
    arr=[list(map(int,list(input()))) for _ in range(16)]
    now=[1,1]
    for i in range(16):
        if 3 in arr[i]:
            goal=[i,arr[i].index(3)]
    stack=[]
    visit=[]
    while now != goal:
        before=now
        for idx,idy in [[1,0],[0,1],[-1,0],[0,-1]]:
            x=now[0]+idx
            y=now[1]+idy
            if 0<=x<16 and 0<=y<16 and arr[x][y] == 0 and [x,y] not in visit:
                stack.append([x,y])
            if arr[x][y]==3:
                stack.append([x,y])
                break
        now=stack[-1]
        if before == now:
            while now in visit:
                stack.pop()
                if not stack:
                    break
                now=stack[-1]
        if not stack:
            break

        visit.append(now)
    if not stack:
        print(f'#{t} 0')
    else:
        print(f'#{t} 1')
