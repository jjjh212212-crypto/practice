import sys
sys.stdin = open("input (3).txt", "r")
for t in range(1,11):
    n=int(input())
    lst=list(input())
    
    operation=[]
    stack=[]
    result=[]
    for i in range(n):
        if lst[i].isdigit():
            stack.append(int(lst[i]))
        else:
            if operation==[]:
                operation.append(lst[i])
            else:
                stack.append(lst[i])
    while operation:
        stack.append(operation.pop())
    while stack:
        a = stack.pop(0)
        if a == '+':
            k1=result.pop()
            k2=result.pop()
            result.append(k1+k2)
        else:
            result.append(a)
    print(f'#{t} {result.pop()}')        
        