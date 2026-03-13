def dfs(N,count):
    global result
    if result <= count:
        return
    if N == 1:
        result = count
        return
    num=N
    c=num%3
    num-=num%3 
    if num != 1:  
        num//=3
        c+=1
    dfs(num,count+c)

    num2=N
    c2=num2%2
    num2-=num2%2
    if num2 != 1:
        num2 //=2
        c2+=1
    dfs(num2,count+c2)
    
def bfs(N):
    global result
    q=[(N,0)]
    while q:
        n,count=q.pop(0)
        if result <= count:
            continue
        if n == 1:
            result = count
            continue
        num=n
        c=num%3
        num-=num%3 
        if num != 1:  
            num//=3
            c+=1
        if result > count+c:
            q.append((num,count+c))
        
        num2=n
        c2=num2%2
        num2-=num2%2
        if num2 != 1:
            num2 //=2
            c2+=1
        if result > count+c2:
            q.append((num2,count+c2))
N=int(input())
result=N
bfs(N)
print(result)



    