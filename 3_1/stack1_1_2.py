import sys

T=int(input())
for t in range(1,T+1):
    lst=list(input())
    stack=[]
    for i in lst:
        if not stack or stack[-1] != i:
            stack.append(i)
        else:
            stack.pop()
    print(f'#{t} {len(stack)}')