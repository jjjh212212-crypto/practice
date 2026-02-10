import sys
sys.stdin = open("input.txt", "r")

for t in range(1,11):
    n=int(input())
    lst=list(input())
    item = [['(','[','{','<'],[')',']','}','>']]
    check=[]
    for j in range(n):
        if lst[j] in item[0]:
            check.append(lst[j])
        elif lst[j] in item[1]:
            idx=item[1].index(lst[j])
            if item[0][idx] == check[-1]:
                check.pop()
            else:
                print(f'#{t} 0')
                break
    if not check:
        print(f'#{t} 1')
        



