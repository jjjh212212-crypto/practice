n=int(input())
stack=[]
for _ in range(n):
    k=input()
    if k=='pop':
        if stack==[]:
            print(-1)
        else:
            print(stack.pop())
    elif k=='size':
        print(len(stack))
    elif k=='empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif k=='top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
    elif k[:4]=='push':
        stack.append(int(k[5:]))