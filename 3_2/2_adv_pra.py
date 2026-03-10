
def dfs(count):
    global result
    # 1. 목표 교환 횟수에 도달하면 결과값 갱신 후 종료
    if count == int(num):
        result = max(result, int("".join(cards)))
        return

    # 2. 현재 상태(숫자 배열 + 남은 횟수)를 문자열로 기록
    current_state = ("".join(cards), count)
    if current_state in visited:
        return
    visited.add(current_state)

    # 3. 모든 경우의 수 교환(완전 탐색)
    n = len(cards)
    for i in range(n):
        for j in range(i + 1, n):
            cards[i], cards[j] = cards[j], cards[i]  
            dfs(count + 1)
            cards[i], cards[j] = cards[j], cards[i]  

T = int(input())

for tc in range(1, T + 1):
    prize_money, num = input().split()
    cards = list(prize_money)
    result = 0
    visited = set()  
    
    dfs(0)
    print(f'#{tc} {result}')