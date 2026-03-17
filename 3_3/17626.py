from math import sqrt
def mx_pro():
    for i in range(int_n,int(sqrt(n/cnt))-1,-1):
        pro(1,1,i**2)
        if bools ==True:
            break
    return bools
def pro(num,start,count):
    global bools
    if bools:
        return
    if num == cnt:
        if count == n:
            bools=True
        return 
    for i in range(start,int(sqrt(count))+1):
        c = count + i**2
        if c > n:
            break
        else:
            pro(num+1,i,c)

n=int(input())
int_n=int(sqrt(n))
mx = int_n ** 2
bools=False
for i in range(1,5):
    cnt=i
    mx_pro()
    if bools:
        result=i
        break
print(result)

        