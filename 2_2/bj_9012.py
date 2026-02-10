n=int(input())
for _ in range(n):
    lst=list(input())
    stack=[]
    b=True
    for i in range(len(lst)):
        if stack==[] and lst[i]==')':
            b=False
            break
        if lst[i]=='(':
            stack.append(lst[i])
        elif lst[i]==')':
            if stack[-1] == '(':
                stack.pop()
            else:
                b=False
    if b and stack==[]:
        print('YES')
    else:
        print('NO')
            
        
    
    