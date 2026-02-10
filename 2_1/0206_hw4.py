T=int(input())
for t in range(1,T+1):
    a=input()
    b=input()
    if a in b:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')