import copy
def board_sort(board):
    for i in range(W):
        count=0
        for j in range(H-1,-1,-1):
            if board[j][i] == 0:
                count+=1
            else:
                board[j][i],board[j+count][i]=board[j+count][i],board[j][i]
    return board
def boom(j,i,board):
    now=board[j][i]
    if now == 0:
        return
    if now == 1:
        board[j][i] = 0
        return
    board[j][i] = 0
    for k in [[1,0],[0,1],[-1,0],[0,-1]]:
        cnt=1
        idx=j+k[0]
        idy=i+k[1]
        while 0<=idx<=H-1 and 0<=idy<=W-1 and cnt < now :
            cnt+=1
            boom(idx,idy,board)
            idx+=k[0]
            idy+=k[1]

def shoot(path,board):
    for i in path:
        for j in range(H):
            if board[j][i] > 0:
                boom(j,i,board)
                board_sort(board)
                break

def product(num):
    global result
    if num == N:
        board=copy.deepcopy(arr)
        shoot(path,board)
        mn=0
        for i in board:
            mn+=i.count(0)
        mn = W*H - mn
        result=min(result,mn)
        return
    
    for i in range(W):
        path.append(i)
        product(num+1)
        path.pop()

T=int(input())
for t in range(1,T+1):
    N,W,H=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(H)]
    path=[]
    result=W*H
    product(0)
    print(f'#{t} {result}')
