import sys
input=sys.stdin.readline
N,M=map(int,input().strip().split())
lst=[input().strip() for _ in range(N)]
for _ in range(M):
    a=input().strip()
    if a.isdigit():
        print(lst[int(a)-1])
    else:
        print(lst.index(a)+1)