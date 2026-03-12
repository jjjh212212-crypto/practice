import copy
import sys
sys.stdin = open("input.txt", "r")
T=int(input())
for t in range(1,T+1):
    lst,b=map(str,input().split())
    lst=[int(i) for i in lst]
    b=int(b)
    i=0
    c=0
    cpy = copy.deepcopy(lst)
    cpy.sort(reverse=True)
    while c != b:
        a=False
        if lst == cpy:
            break
        if lst[i] == cpy[i]:
            i+=1
            continue
        else:
            for j in range(i+1,len(lst)):
                if lst[i] == cpy[j] and lst[j] == cpy[i]:
                    lst[i],lst[j] = lst[j],lst[i]
                    i+=1
                    c+=1
                    a=True
                    break
            if not a:
                for j in range(len(lst)-1,i,-1):
                    if lst[j] == max(lst[i:]):
                        lst[i],lst[j] = lst[j],lst[i]
                        i+=1
                        c+=1
                        break
    

    if (b-c) % 2 == 1 and len(lst) == len(set(lst)):
        lst[-1],lst[-2] = lst[-2],lst[-1]

    print(f'#{t}',''.join(map(str,lst)))


