import sys
input=sys.stdin.readline

N,M=map(int,input().strip().split())
lst=list(map(int,input().strip().split()))
lst2=[0]*N
lst2[0] = lst[0]
for i in range(1,len(lst)): 
    lst2[i] = lst[i] + lst2[i-1]
for _ in range(M):
    i,j=map(int,input().strip().split())
    if i == 1:
        print(lst2[j-1])
    else:
        print(lst2[j-1]-lst2[i-2])