import sys
sys.stdin = open("input (4).txt", "r")
for t in range(1,11):
    n=int(input())
    lst=list(input())
    rank=[['+','*'],[1,2]]
    operation=[]
    stack=[]
    result=[]
    for i in range(n):
        if lst[i].isdigit():
            stack.append(int(lst[i]))
        else:
            if operation==[] or rank[1][rank[0].index(lst[i])]>rank[1][rank[0].index(operation[-1])]:
                operation.append(lst[i])
            elif rank[1][rank[0].index(lst[i])]<=rank[1][rank[0].index(operation[-1])]:
                while operation!=[] and rank[1][rank[0].index(lst[i])]<=rank[1][rank[0].index(operation[-1])]:
                    stack.append(operation.pop())
                operation.append(lst[i])
            else:
                stack.append(lst[i])
    while operation:
        stack.append(operation.pop())
    while stack:
        a = stack.pop(0)
        if a == '+' :
            k1=result.pop()
            k2=result.pop()
            result.append(k1+k2)
        elif a== '*':
            k1=result.pop()
            k2=result.pop()
            result.append(k1*k2)
        else:
            result.append(a)
    print(f'#{t} {result.pop()}')     