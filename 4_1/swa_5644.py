from collections import deque
import sys
sys.stdin = open("sample_input (1).txt", "r")
def bfs(x,y,w):
    que=deque()
    que.append((x,y,0))
    visit = [[0]*10 for _ in range(10)]
    visit[y][x] = 1
    result=[]
    while que:
        dx,dy,dw=que.popleft()
        result.append((dx,dy))
        for i in range(1,5): 
            idx=dx+nx[i]
            idy=dy+ny[i]
            if 0<=idx<10 and 0<=idy<10:
                if not visit[idy][idx] and dw < w:
                    que.append((idx,idy,dw+1))
                    visit[idy][idx] = 1
    return result

def max_value(user1,user2):
    result1=0
    if not dic_AP[user1] and not dic_AP[user2]:
        return 0
    elif not dic_AP[user1]:
        for i in dic_AP[user2]:
            if power_AP[i] > result1:
                result1 = power_AP[i]

    elif not dic_AP[user2]:
        for i in dic_AP[user1]:
            if power_AP[i] > result1:
                result1 = power_AP[i]

    else:
        for i in dic_AP[user1]:
            for j in dic_AP[user2]:
                if i != j and result1 < power_AP[i]+power_AP[j]:
                    result1 = power_AP[i]+power_AP[j]
                elif i == j and result1 < power_AP[i]:
                    result1 = power_AP[i]
    
    return result1


ny=[0,-1,0,1,0]
nx=[0,0,1,0,-1]
T=int(input())
for t in range(1,T+1):
    M,A=map(int,input().split())
    lst1=[0]+list(map(int,input().split()))
    lst2=[0]+list(map(int,input().split()))
    power_AP=[]
    dic_AP={}
    for i in range(10):
        for j in range(10):
            dic_AP[(i,j)]=[]

    for i in range(A):
        x,y,w,p= map(int,input().split())
        power_AP.append(p)
        BC = bfs(y-1,x-1,w)
        for j in BC:
            dic_AP[j].append(i)
    
    print(power_AP)
    x1,y1 = 0,0
    x2,y2 = 9,9
    max_sum=0
    for i in range(M+1):
        x1 += nx[lst1[i]]
        y1 += ny[lst1[i]]
        x2 += nx[lst2[i]]
        y2 += ny[lst2[i]]
        max_sum+=max_value((y1,x1),(y2,x2))
    print(f'#{t} {max_sum}')
