# import sys
# input=sys.stdin.readline

# n=int(input().strip())
# a=[]
# result=[]
# stack=[]
# for _ in range(n):
#     result.append(int(input().strip()))

# count=0
# for i in range(n):
#     if result[i] not in stack:
#         while count != result[i]:
#             a.append('+')
#             count+=1
#             stack.append(count)
#     if stack[-1] == result[i]:
#         a.append('-')
#         stack.pop()
#     else:
#         break
# if not stack:
#     for i in a:
#         print(i)
# else:
#     print('NO')
import sys
input=sys.stdin.readline
n=int(input().strip())
stack=[]
result=[]
max=0
tf=True
for i in range(n):
    a=int(input().strip())
    if not stack or stack[-1] < a:
        for j in range(max+1,1+a):
            result.append('+')
            stack.append(j)
        b=stack.pop()
        if max < b:
            max=b
        result.append('-')
    elif stack[-1] == a:
        stack.pop()
        result.append('-')
    else:
        tf=False
if not tf:
    print('NO')
else:
    for i in result:
        print(i)

    


