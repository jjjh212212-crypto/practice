# def cal(i):
#     global result
#     global minusnum
#     if isinstance(stack[i],int):
#         if bools:
#             ready.append(stack[i])
#         else:
#             minus.append(stack[i])
#     elif stack[i] == '+':
#         if bools:
#             result+=ready.pop()
#         else:
#             minusnum+=minus.pop()
    
# a=list(input())
# b=''
# stack=[]
# for i in a:
#     if i.isdigit():
#         b+=i
#     else:
#         stack.append(int(b))
#         stack.append(i)
#         b=''
# stack.append(int(b))
# print(stack)
# result=0
# ready=[]
# minus=[]
# i=0
# bools=True
# while i < len(stack):
#     if stack[i] == '-':
#         bools=False
#         i+=1
#         minusnum=0
#         while i < len(stack) and stack[i] != '-':
#             cal(i)
#             i+=1
#         minusnum+=minus.pop()
#         result-=minusnum
#         bools=True
#     else:
#         cal(i)
#         i+=1
# result+=ready.pop()
# print(result)

#otherpeople
s = input()

part = s.split("-")
print(part)
result = sum(map(int,part[0].split("+")))
print(result)
for p in part[1:]:
    result -= sum(map(int, p.split('+')))

print(result)