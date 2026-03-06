import sys
sys.stdin = open("input (1).txt", "r")
T=int(input())
for t in range(1,T+1):
    N,M=map(int,input().split())
    arr=[input() for _ in range(N)]
    for i in arr:
        if '1' in i:
            i=i.strip('0')
            a=i
            break
    if len(a) == 53:
        a ='000'+a
    elif len(a) == 54:
        a = '00'+a
    elif len(a) == 55:
        a = '0'+a
    b=0
    r=0
    for i in range(8):
        k=a[7*i:7*(i+1)]
        if k == '0001101':
            c=0
        elif k == '0011001':
            c=1
        elif k == '0010011':
            c=2
        elif k == '0111101':
            c=3
        elif k == '0100011':
            c=4
        elif k == '0110001':
            c=5
        elif k == '0101111':
            c=6
        elif k == '0111011':
            c=7
        elif k == '0110111':
            c=8
        elif k == '0001011':
            c=9
        if i%2==0:
            b+=3*c
            r+=c
        else:
            b+=c
            r+=c
    if b%10 == 0:
        print(f'#{t} {r}')
    else:
        print(f'#{t} 0')
