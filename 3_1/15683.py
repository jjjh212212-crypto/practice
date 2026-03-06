import itertools
import copy
N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
def cctv(i,j):
    cctv0=[]
    for k in [[1,0],[0,-1],[-1,0],[0,1]]:
        cctv1=[]
        idx=i+k[0]
        idy=j+k[1]
        while 0<=idx<N and 0<=idy<M and arr[idx][idy] !=6:
            cctv1.append((idx,idy))
            idx+=k[0]
            idy+=k[1]
        cctv0.append(cctv1)
    return cctv0
pro=[]
nums=[]
result1=[]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 6 :
            result1.append((i,j))
        elif 0 < arr[i][j] < 6:
            result1.append((i,j))
            pro.append(cctv(i,j))
            nums.append(arr[i][j])
mx=0
for i in itertools.product([0,1,2,3],repeat=len(nums)):
    result=copy.deepcopy(result1)
    for j in range(len(nums)):
        if nums[j] == 1:
            result+=pro[j][i[j]]
        elif nums[j] == 2:
            k=i[j]%2
            result+=pro[j][k]
            result+=pro[j][k+2]
        elif nums[j] == 3:
            result+=pro[j][i[j]]
            result+=pro[j][(i[j]+1)%4]
        elif nums[j] == 4:
            result+=pro[j][i[j]]
            result+=pro[j][(i[j]+1)%4]
            result+=pro[j][(i[j]+2)%4]
        elif nums[j] == 5:
            result+=pro[j][0]
            result+=pro[j][1]
            result+=pro[j][2]
            result+=pro[j][3]
    result=set(result)
    if mx <= len(result):
        mx = len(result)
print(N*M-mx)
