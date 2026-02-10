import sys
sys.stdin = open("input (1).txt", "r")

for t in range(1,11):
    t=input()
    arr=[list(input()) for _ in range(100)]
    max=0
    for n in range(100,0,-1):  # i 가 100부터 회문 세기
        for _ in range(2):     # 전치해서 확인
            for i in range(100):  # 행 검사
                for j in range(101-n):  # 한행에서 i인 길이 옆으로 움직이면서 세기
                    count=0
                    for k in range(n//2): # 
                        if arr[i][j:j+n][k] != arr[i][j:j+n][n-k-1]:
                            break
                        else:
                            count+=1
                    if count == n//2:
                        max = n
                        break
                if max==n:
                    break
            if max==n:
                break
            arr=list(map(list,zip(*arr)))
        if max==n:
            break
    print(max)

