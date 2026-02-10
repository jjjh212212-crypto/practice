def un15(j):
    global mx
    if j % 5 ==0:
        mx+=j//5
    elif j % 3==0:
        mx+=j//3
    elif j == 8:
        mx+=2
    elif j==11:
        mx+=3
    elif j==13:
        mx+=3
    elif j==14:
        mx+=4
n=int(input())
k=[1,2,4,7]
mx=0
if n in k:
    print(-1)
elif n>15:
    c=n//15 
    m=n-(c-1)*15 # 16~30 사이 값
    l=m%15 # 
    mx+=(15*(c-1))//5
    if l in k:
        if l == 1:
            mx+=4
        elif l==2:
            mx+=5
        elif l==4:
            mx+=5
        elif l==7:
            mx+=6
    else:
        mx+=3
        j=m-15
        un15(j)
else:
    un15(n)

print(mx)