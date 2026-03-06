for t in range(1,11):
    N,M=map(str,input().split())
    stack=[]
    for i in M:
        if not stack or stack[-1]!=i:
            stack.append(i)
        else:
            stack.pop()
    print(f'#{t}',''.join(stack))