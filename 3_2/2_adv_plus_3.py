import math
T=int(input())
for t in range(1,T+1):
    N=int(input())
    i=1
    while True:
        i_3=i**3
        if i_3 < N:
            i+=1
        elif i_3 == N:
            print(f'#{t} {i}')
            break
        else:
            print(f'#{t} -1')    
            break
    