T=int(input())
for t in range(1,T+1):
    arr=[list(map(int,input().split())) for _ in range(9)]
    row=[]
    for i in range(9):
        row.append(sum(arr[i]))
    col=[]
    for i in range(9):
        col.append(sum([arr[j][i] for j in range(9)]))
    rec=[]
    for i in range(3):
        for j in range(3):
            rec.append(sum([arr[3*i+k][3*j+h] for k in range(3) for h in range(3)]))
    if row==col==rec==[45]*9:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')
