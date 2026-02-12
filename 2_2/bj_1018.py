N,M=map(int,input().split())
arr=[list(input()) for _ in range(N)]

for i in range(N-7):
    for j in range(M-7):
        count=0
        for k in range(8):
            if k%2==0:
                for h in range(8):
                    if h%2==0:
                        if arr[i+k][j+h] != 'W':
                            count+=1
                    else:
                        if arr[i+k][j+h] != 'B':
                            count+=1
            else:
                for h in range(8):
                    if h%2==0:
                        if arr[i+k][j+h] != 'B':
                            count+=1
                    else:
                        if arr[i+k][j+h] != 'W':
                            count+=1
        if i == j == 0:
            min = count
        if count < min:
            min = count
        count=0
        for k in range(8):
            if k%2==0:
                for h in range(8):
                    if h%2==0:
                        if arr[i+k][j+h] != 'B':
                            count+=1
                    else:
                        if arr[i+k][j+h] != 'W':
                            count+=1
            else:
                for h in range(8):
                    if h%2==0:
                        if arr[i+k][j+h] != 'W':
                            count+=1
                    else:
                        if arr[i+k][j+h] != 'B':
                            count+=1

        if count < min:
            min = count
print(min)