def left(arr):
    global N
    for k in range(N):
        for h in range(N):
            if arr[k][h] == 0:
                for i in range(h+1,N):
                    if arr[k][i] > 0:
                        arr[k][h], arr[k][i] = arr[k][i], arr[k][h]
                        break
    return arr

def left_sort(arr):
    global N
    for k in range(N):
        i=0
        while i < N-1:
            if arr[k][i] == 0:
                break    
            if arr[k][i] == arr[k][i+1]:
                arr[k][i] *=2
                arr[k][i+1] = 0
                i+=2
            else:
                i+=1
            # if i == N-1 or i == N:
            #     break
    return left(arr)

def right(arr):
    global N
    for k in range(N):
        for h in range(N-1,-1,-1):
            if arr[k][h] == 0:
                for i in range(h-1,-1,-1):
                    if arr[k][i] > 0:
                        arr[k][h], arr[k][i] = arr[k][i], arr[k][h]
                        break
    return arr

def right_sort(arr):
    global N
    for k in range(N):
        i=N-1
        while i > 0:
            if arr[k][i] == 0:
                break    
            if arr[k][i] == arr[k][i-1]:
                arr[k][i] *=2
                arr[k][i-1] =0
                i-=2
            else:
                i-=1
            # if i == 0 or i == -1:
            #     break
    return right(arr)

import itertools
import copy

N=int(input())
arr1=[list(map(int,input().split())) for _ in range(N)]
result = 0
for i in itertools.product(['u','d','l','r'],repeat=5):
    arr = copy.deepcopy(arr1)
    for j in range(5):
        if i[j] == 'u':
            arr = [list(row) for row in zip(*arr)]
            arr = left(arr)
            arr = left_sort(arr)
            arr = [list(row) for row in zip(*arr)]

        elif i[j] == 'd':
            arr = [list(row) for row in zip(*arr)]
            arr = right(arr)
            arr = right_sort(arr)
            arr = [list(row) for row in zip(*arr)]

        elif i[j] == 'l':
            arr = left(arr)
            arr = left_sort(arr)
        elif i[j] == 'r':
            arr = right(arr)
            arr = right_sort(arr)
    mx=0
    for i in arr:
        if mx <= max(i):
            mx = max(i)
    if mx >= result:
        result = mx
print(result)

        

