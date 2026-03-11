import sys
sys.stdin = open("input (1).txt", "r")
def merge(left,right):
    l=r=0
    result = [0] * (len(left)+len(right))
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l+r] = left[l]
            l+=1
        else:
            result[l+r] = right[r]
            r+=1
    while l < len(left):
        result[l+r]=left[l]
        l+=1
    while r < len(right):
        result[l+r]=right[r]
        r+=1
    return result
    
def merge_sort(lst):
    if len(lst) == 1:
        return lst
    mid = len(lst)//2
    
    left_list = merge_sort(lst[:mid])
    right_list = merge_sort(lst[mid:])
    merge_list = merge(left_list,right_list)

    return merge_list
lst=list(map(int,input().split()))
print(merge_sort(lst)[500000])
# lst=list(map(int,input().split()))
# lst.sort()
# print(lst[500000])