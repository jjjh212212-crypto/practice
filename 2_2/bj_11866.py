N,K=map(int,input().split())
num=[i for i in range(1,N+1)]
stack=[]
n=K-1
for _ in range(N):
    stack.append(num.pop(n))
    if len(num)==0:
        break
    n=(n+K-1)%len(num)
print('<',end='')
for i in range(len(stack)):
    if i == len(stack)-1:
        print(stack[i], end='')
    else:
        print(stack[i], end=', ')
print('>') 