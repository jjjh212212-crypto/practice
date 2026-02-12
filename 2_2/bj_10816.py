import sys
input = sys.stdin.readline

N=int(input())
lstN=list(map(int,input().split()))
M=int(input())
lstM=list(map(int,input().split()))
result={}
for i in lstN:
    if i in result:
        result[i]+=1
    else:
        result[i]=1
for i in lstM:
    if i in result:
        print(result[i], end=' ')
    else:
        print(0,end=' ')