import sys
input=sys.stdin.readline
n=int(input())
lst=[int(input()) for _ in range(n)]
if n!=0:
    lst.sort()
    e15=int((n*15)/100+0.5)
    if e15 != 0:
        print(int(sum(lst[e15:-e15])/(n-2*e15)+0.5))
    else:
        print(int((sum(lst)/(n))+0.5))
else:
    print(n)
