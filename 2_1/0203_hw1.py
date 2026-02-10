T=int(input())
for test_case in range(1,T+1):
    a,b=map(int,input().split())
    lsta=list(map(int,input().split()))
    lstb=list(map(int,input().split()))
    s=0
    count=0
    for i in range(b):
        for j in range(s,a):
            if lsta[j]==lstb[i]:
                count+=1
                s=j+1
                break
    if count==len(lstb):
        print(f'#{test_case} YES')
    else:
        print(f'#{test_case} NO')