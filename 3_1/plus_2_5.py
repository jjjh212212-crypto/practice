T=int(input())
for t in range(1,T+1):
    lst=list(input())
    stack=[]
    count=0
    for i in lst:
        if i == '(':
            stack.append(i)
            a=True
        elif i ==')':
            if a:
                stack.pop()
                count+=len(stack)
                a=False
            else:
                stack.pop()
                count+=1
    print(f'#{t} {count}')