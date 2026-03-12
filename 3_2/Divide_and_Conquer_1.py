def hoare_partition(left,right): 
    pivot=lst[left]
    i = left + 1
    j = right

    while i <= j:
        while i <= j and lst[i] <= pivot:
            i+=1
        while i <= j and lst[j] >= pivot:
            j-=1
        
        if i < j:
            lst[i],lst[j] = lst[j],lst[i]
    lst[left], lst[j] = lst[j], lst[left]
    return j
def quick_sort(left,right):
    if left < right:
        pivot = hoare_partition(left,right)
        quick_sort(left,pivot-1)
        quick_sort(pivot+1,right)


T=int(input())
for t in range(1,T+1):
    N=int(input())
    lst=list(map(int,input().split()))
    quick_sort(0,len(lst) - 1)
    print(f'#{t} {lst[N//2]}')


    