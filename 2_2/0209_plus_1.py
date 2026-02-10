T=int(input())
for t in range(1,T+1):
#     a=input()
#     count=0
#     for i in range(len(a)-1):
#         cl=0
#         cr=0
#         if a[i]=='(':
#             j=i
#             while cl!=cr or cl==cr==0:
#                 if a[j]=='(':
#                     cl+=1
#                 elif a[j]==')':
#                     cr+=1
#                 j+=1    
#             raiser=a[i+1:j].count('()')
#             if raiser>0:
#                 count+=a[i+1:j].count('()')+1
#     print(f'#{t} {count}')
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