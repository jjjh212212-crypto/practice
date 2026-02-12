import sys
sys.stdin = open("sample_input (2).txt", "r")
T=int(input())
for t in range(1,T+1):
    N=int(input())
    miro=[list(map(int,list(input()))) for _ in range(N)]
    for i in range(N):
        if 2 in miro[i]:
            start=[i,miro[i].index(2)]
        if 3 in miro[i]:
            goal=[i,miro[i].index(3)]
    stack=[start]
    visit=[start]
    now=start
    while stack[-1] != goal:
        before=now
        for idx,idy in [[0,1],[1,0],[-1,0],[0,-1]]:
            if 0 <= now[0]+idx < N and 0 <= now[1]+idy < N:
                if miro[now[0]+idx][now[1]+idy] == 0 and [now[0]+idx,now[1]+idy] not in visit and [now[0]+idx,now[1]+idy] not in stack:
                    stack.append([now[0]+idx,now[1]+idy])
                if miro[now[0]+idx][now[1]+idy] == 3:
                    stack.append([now[0]+idx,now[1]+idy])
        if stack[-1] == goal:
            print(f'#{t} 1')
            break
        now=stack[-1]
        l=len(stack)
        if before == now:
            while stack[-1] in visit:
                stack.pop()
                if not stack:
                    break

        if not stack or l == len(stack) and before == now:
            print(f'#{t} 0')
            break            
        now=stack[-1]
        visit.append(now)
        

