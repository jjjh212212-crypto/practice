T=int(input())
for t in range(1,T+1):
    N,M,K=map(int,input().split())
    arr=[[0]*M for _ in range(N)]
    for _ in range(K):
        a,b=map(int,input().split())
        arr[a][b]=1
    visit=set()
    idx=[1,0,-1,0]
    idy=[0,1,0,-1]
    count=0
    for i in range(N):
        for j in range(M):
            stack=[]
            if arr[i][j]==1 and (i,j) not in visit:
                stack.append((i,j))
                while stack:
                    x,y = stack.pop()
                    visit.add((x,y))
                    for k in range(4):
                        xx=x+idx[k]
                        yy=y+idy[k]
                        if 0<=xx<N and 0<=yy<M and arr[xx][yy] == 1 and (xx,yy) not in stack and (xx,yy) not in visit:
                            stack.append((xx,yy))
                count+=1
    print(count)
    
                    

