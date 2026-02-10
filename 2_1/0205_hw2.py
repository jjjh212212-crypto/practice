T=int(input())
for t in range(1,T+1):
    P,A,B= map(int,input().split())
    lA=1
    rA=P
    lB=1
    rB=P
    a=0
    b=0
    while True:
        cA=int((lA+rA)/2)
        cB=int((lB+rB)/2)
        if A == cA:
            a=1
        elif lA <= A < cA:
            rA=cA
        elif cA < A <= rB:
            lA=cA

        if B == cB:
            b=1 
        elif lB <= B < cB:
            rB=cB
        elif cB <= B <= rB:
            lB=cB
        
        if a==b==1:
            print(f'#{t} 0')
            break
        elif a==1:
            print(f'#{t} A')
            break
        elif b==1:
            print(f'#{t} B')
            break
    