import sys
sys.stdin = open("sample_input (1).txt", "r")
T=int(input())
for t in range(1,T+1):
    lst=list(input().split())
    stack=[]
    for i in range(len(lst)):
        if lst[i].isdigit():
            stack.append(int(lst[i]))
        elif lst[i]=='+' or lst[i]=='*' or lst[i]=='-' or lst[i]=='/':
            if len(stack)<=1:
                stack.pop()
                break
            a=stack.pop()
            b=stack.pop()
            if lst[i]=='+':
                stack.append(b+a)
            elif lst[i]=='/':
                stack.append(b//a)
            elif lst[i]=='*':
                stack.append(b*a)
            elif lst[i]=='-':
                stack.append(b-a)
    if not stack or len(stack) >=2:
                print(f'#{t} error')
    else:
        print(f'#{t} {stack.pop()}')
       