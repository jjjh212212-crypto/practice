N=int(input())
lst=list(map(int,input().split()))
stack=[lst[0]]
idx=[1]
print(0,end=' ')
for i in range(1,N): 
    if stack[-1] <= lst[i]:
        while stack and stack[-1] <= lst[i]:
            stack.pop()
            idx.pop()
    if not stack:
        print(0,end=' ')
    else:
        print(idx[-1],end=' ')

    stack.append(lst[i])
    idx.append(i+1)

         