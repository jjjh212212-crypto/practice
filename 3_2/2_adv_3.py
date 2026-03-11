def merge(left,right):
    global count
    result = [0] * (len(left) + len(right))
    l = r = 0
    if left[-1] > right[-1]:
        count+=1
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l+r]=left[l]
            l+=1
        else:
            result[l+r]=right[r]
            r+=1
    while l < len(left):
        result[l+r] = left[l]
        l+=1
    while r < len(right):
        result[l+r]=right[r]
        r+=1
    
    return result

def merge_sort(li):
    if len(li) == 1:
        return li
    mid = len(li)//2
    left_list = merge_sort(li[:mid])
    right_list = merge_sort(li[mid:])

    merge_list= merge(left_list,right_list)
    return merge_list

T=int(input())
for t in range(1,T+1):
    N=int(input())
    lst=list(map(int,input().split()))
    count=0
    print(f'#{t}',merge_sort(lst)[N//2],count)