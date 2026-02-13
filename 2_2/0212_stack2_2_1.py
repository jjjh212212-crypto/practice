def battle(arr):
    if len(arr[0]) %2==0:
        k=0
    else:
        k=1
    for i in range(k,len(arr[0])//2):
        a=arr[0][i]
        b=arr[0][i+1]
        if a-b==-2 or a>=b and a-b!= 2:
            arr[0].pop(i+1)
            arr[1].pop(i+1)
        else:
            arr[0].pop(i)
            arr[1].pop(i)
    return arr
def tonament(a):
    l=len(a[0])
    if l == 1:
        return a
    arr1=[a[0][:l//2],a[1][:l//2]]
    arr2=[a[0][l//2:],a[1][l//2:]]
    tonament(battle(arr1))[0].append(tonament(battle(arr2))[0])
    tonament(battle(arr1))[1].append(tonament(battle(arr2))[1])
    return tonament(arr1)
T=int(input())
for t in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split()))]
    arr.append([i for i in range(1,N+1)])
    tonament(arr)
    print(f'#{t} {arr[1].pop()}')