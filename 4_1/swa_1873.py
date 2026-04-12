def move(x,y,v):
    idx=x+nx[v]
    idy=y+ny[v]
    if 0<=idx<W and 0<=idy<H and arr[idy][idx] == '.':
        arr[y][x]='.'
        arr[idy][idx]=dic[v]
        return(idx,idy,v)
    else:
        arr[y][x]=dic[v]
        return(x,y,v)

def shoot(x,y,v):
    idx=x
    idy=y
    while True:
        idx+=nx[v]
        idy+=ny[v]
        if 0<=idx<W and 0<=idy<H:
            check = arr[idy][idx]
            if check == '#':
                break
            elif check == '*':
                arr[idy][idx] = '.'
                break
        else:
            break
    return (x,y,v)

def user_act(x,y,v,k):
    if k != 'S':
        if k == 'U':
            v=0
        elif k == 'D':
            v=2
        elif k == 'L':
            v=3
        elif k == 'R':
            v=1
        return move(x,y,v)
    else:
        return shoot(x,y,v)

ny=[-1,0,1,0]
nx=[0,1,0,-1]
dic={
    0:'^',
    1:'>',
    2:'v',
    3:'<'
}
T=int(input())
for t in range(1,T+1):
    H,W=map(int,input().split())
    arr=[list(input().strip()) for _ in range(H)]
    N=int(input())
    lst=list(input())
    for i in range(H):
        for j in range(W):
            if arr[i][j] == '>':
                x=j
                y=i
                vector=1
            elif arr[i][j] == '<':
                x=j
                y=i
                vector=3
            elif arr[i][j] == '^':
                x=j
                y=i
                vector=0
            elif arr[i][j] == 'v':
                x=j
                y=i
                vector=2
                break
# .	평지(전차가 들어갈 수 있다.)
# *	벽돌로 만들어진 벽
# #	강철로 만들어진 벽
# -	물(전차는 들어갈 수 없다.)
# ^	위쪽을 바라보는 전차(아래는 평지이다.)
# v	아래쪽을 바라보는 전차(아래는 평지이다.)
# <	왼쪽을 바라보는 전차(아래는 평지이다.)
# >	오른쪽을 바라보는 전차(아래는 평지이다.)


# U	Up : 전차가 바라보는 방향을 위쪽으로 바꾸고, 한 칸 위의 칸이 평지라면 위 그 칸으로 이동한다.
# D	Down : 전차가 바라보는 방향을 아래쪽으로 바꾸고, 한 칸 아래의 칸이 평지라면 그 칸으로 이동한다.
# L	Left : 전차가 바라보는 방향을 왼쪽으로 바꾸고, 한 칸 왼쪽의 칸이 평지라면 그 칸으로 이동한다.
# R	Right : 전차가 바라보는 방향을 오른쪽으로 바꾸고, 한 칸 오른쪽의 칸이 평지라면 그 칸으로 이동한다.
# S	Shoot : 전차가 현재 바라보고 있는 방향으로 포탄을 발사한다.
    for i in lst:
        x,y,vector = user_act(x,y,vector,i)
    print(f'#{t}',end=' ')
    for i in arr:
        print(''.join(i))