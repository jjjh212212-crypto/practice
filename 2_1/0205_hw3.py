T=int(input())
for t in range(1,T+1):
    N=int(input())
    lst=list(map(int,input().split()))
    for i in range(N-1):
        max_idx=i
        min_idx=i
        if i%2==0:
            for j in range(i+1,N):
                if lst[max_idx] < lst[j]:
                    max_idx = j
            lst[i],lst[max_idx] = lst[max_idx],lst[i]
        else:
            for j in range(i+1,N):
                if lst[min_idx] > lst[j]:
                    min_idx = j
            lst[i],lst[min_idx] = lst[min_idx],lst[i]
    
    print(f'#{t}',*lst[:10]) 

# for t in range(1,T+1):
#     N=int(input())
#     lst=list(map(int,input().split()))
#     for i in range(N):
#         max=lst[-1]
#         min=lst[-1]
#         max_index=-1
#         min_index=-1
#         if i%2==0:
#             for j in range(i,N):
#                 if max <= lst[j]:
#                     max = lst[j]
#                     max_index = j
#             lst[i],lst[max_index] = lst[max_index],lst[i]
#         else:
#             for j in range(i,N):
#                 if min >= lst[j]:
#                     min = lst[j]
#                     min_index = j
#             lst[i],lst[min_index] = lst[min_index],lst[i]
#     print(f'#{t}',*lst) 