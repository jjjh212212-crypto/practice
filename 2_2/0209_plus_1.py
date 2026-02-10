T=int(input())
for t in range(1,T+1):
    a=input()
    count=0
    l=0
    for i in range(len(a)):
        if a[i] == '(':
            l+=1
        elif a[i-1]+a[i] == '))':
            l-=1
            count+=1
        elif a[i]==')':
            l-=1
            count+=l
    print(count)