T=int(input())
for t in range(1,1+T):
    N=int(input())
    arr=[[0]*N for _ in range(N)]
    vector=['E','S','W','N'] 
    for i in range(N):
        arr[0][i]=i+1
    k=1
    z=1
    x=0
    y=N-1
    n=N
    for _ in range((N-1)*2):
        for _ in range(2):
            vec=vector[z%4]
            for j in range(N-k):
                n+=1
                if vec == 'E':
                    y+=1
                elif vec == 'S':
                    x+=1
                elif vec == 'W':
                    y-=1
                else:
                    x-=1
                arr[x][y]=n
            z+=1
        k+=1
    print(f'#{t}')
    for i in range(N):
        print(*arr[i])
    
            

            


