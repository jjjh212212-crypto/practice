import sys
input=sys.stdin.readline

n=int(input().strip())
a=[]
result=[]
stack=[]
for _ in range(n):
    result.append(int(input().strip()))

count=0
for i in range(n):
    if result[i] not in stack:
        while count != result[i]:
            a.append('+')
            count+=1
            stack.append(count)
    if stack[-1] == result[i]:
        a.append('-')
        stack.pop()
    else:
        break
if not stack:
    for i in a:
        print(i)
else:
    print('NO')
    

