T=int(input())
for i in range(1,T+1):
    K,N,M = map(int,input().split())
    lst=list(map(int,input().split()))
    count=0    # 충전 횟수
    start=0   # 정류장 출발 위치 
    j=0       # 충전소 인덱스
    while True:
        start0=start   # start0 = 출발하기 전 위치  
        while lst[j]<=start+K:  # 충전소 위치가 (정류장 출발 위치 + K(이동 거리)) 보다 작을때 while문
            j+=1                # 다음 충전소 위치까지 갈 수 있는지 검사 하기 위해 인덱스 값+1
            if j == M:          # 충전소의 위치 값이 충전소의 갯수와 같으면 while문 break
                break           # 이유 : 마지막 인덱스가 성립하면 그 다음 인덱스도 while문에 돌아가서 오류발생
        start=lst[j-1]  # start = 이동 치치 위치
        count+=1        # 충전횟수 +1
        if start0 == start:     # 출발하기 전 위치와 이동 후 위가 같다면 움직이지 못했단 말이므로
            print(f'#{i} 0')    # 0을 출력하고 break
            break
        if N-start<=K:          # 정류장 전체길이에서 현재위치를 뺀 값이 이동 거리보다 짧으면
            print(f'#{i} {count}') # 한번에 도착 가능하므로 count 출력하고 break
            break