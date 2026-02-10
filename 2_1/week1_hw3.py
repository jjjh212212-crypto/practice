def check(arr):
    global K
    count=0
    for i in arr:
        for j in range(len(i)-K+1):
            if j==0:
                if i[:K+1] == [1]*K+[0]:
                    count+=1
            elif j==len(arr)-K:
                if i[-K-1:] ==[0]+[1]*K:
                    count+=1
            else:
                if i[j-1:j+K+1]==[0]+[1]*K+[0]:
                    count+=1
    return count

T=int(input())
for t in range(1,T+1):
    N,K=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    count=0
    count+=check(arr)
    for i in range(N):
        for j in range(N):
            if i<j:
                arr[i][j],arr[j][i] = arr[j][i],arr[i][j]
    count+=check(arr)
    print(count)



    