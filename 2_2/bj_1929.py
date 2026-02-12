N,M = map(int,input().split())
result=[i for i in range(2,M+1)]
sqrt=int(M**0.5)
i=0
while result[i] <= sqrt:
    result = [x for x in result if x%result[i]!=0 or x==result[i]]
    i+=1
result = [x for x in result if x>=N]
for i in result:
    print(i)

