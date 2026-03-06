N,M=map(int,input().split())
lst=[int(input()) for _ in range(N)]
count=0
lst.sort()
while M != 0:
    lst=[i for i in lst if i <= M]
    count+=M//lst[-1]
    M%=lst[-1] 
print(count)    

