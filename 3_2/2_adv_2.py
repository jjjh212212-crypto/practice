import copy
T=int(input())
for t in range(1,T+1):
    lst=list(map(int,input().split()))
    stack1=[]
    stack2=[]
    run0 = [''.join(map(str,[i,i+1,i+2])) for i in range(8)]
    triple0 = [''.join(map(str,[i,i,i])) for i in range(10)]
    a=0
    for i in range(12):
        if i % 2 == 0:
            stack1.append(lst[i])
        else:
            stack2.append(lst[i])
        if len(stack1) >= 3 or len(stack2) >= 3:
            stack1.sort()
            stack2.sort()
            st_1 = ''.join(map(str,stack1))
            st_2 = ''.join(map(str,stack2))
            for i in triple0:
                if i in st_1:
                    a=1
                    break
                elif i in st_2:
                    a=2
                    break
            cpy1=copy.deepcopy(stack1)
            cpy2=copy.deepcopy(stack2)
            cpy1=list(set(cpy1))
            cpy2=list(set(cpy2))
            cpy1.sort()
            cpy2.sort()
            cpy1=''.join(map(str,cpy1))
            cpy2=''.join(map(str,cpy2))
            for i in run0:
                if i in cpy1:
                    a=1
                    break
                elif i in cpy2:
                    a=2
                    break
        if a!=0:
            break
                    
    print(f'#{t} {a}')
