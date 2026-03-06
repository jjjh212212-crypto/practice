for t in range(1,11):
    N=int(input())
    lst=list(input())
    stack=[]
    bracket=[['(','[','{','<'],[')',']','}','>']]
    result=True
    for i in lst:
        if i in bracket[0]:
            stack.append(i)
        elif i in bracket[1]:
            if stack:
                if bracket[0].index(stack[-1]) == bracket[1].index(i):
                    stack.pop()
                else:
                    result=False
                    break
            else:
                result=False
                break
    if stack or result==False:
        print(f'#{t} 0')
    else:
        print(f'#{t} 1')
