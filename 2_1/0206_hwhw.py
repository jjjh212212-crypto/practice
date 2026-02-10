import sys
sys.stdin = open("GNS_test_input.txt", "r")

T=int(input())
for t in range(1,T+1):
    n=int(list(input().split())[1])
    lst=list(input().split())
    s=0
    num=["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    for i in range(10):
        for j in range(s,n):
            if lst[j] == num[i]:
                lst[s] , lst[j] = lst[j], lst[s]
                s+=1
    print(f'#{t}')
    print(*lst)



