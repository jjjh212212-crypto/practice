n=int(input())
k=[]
for i in range(n):
    a=int(input())
    if a!=0:
        k.append(a)
    elif a==0 and k==[]:
        continue
    else:
        k.pop()
print(sum(k))