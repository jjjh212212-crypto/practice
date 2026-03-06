import sys
import itertools

input = sys.stdin.readline
N=int(input().strip())
arr = [list(map(int,input().strip().split())) for _ in range(N)]
sm=0
for h in itertools.permutations(range(1,9),8):
    lineup = h[:3] + (0,) + h[3:]
    k = 0
    score = 0
    for i in arr:
        count = 0
        b1 = b2 = b3 = 0
        while count != 3:
            hitter = lineup[k]
            hit = i[hitter]
            if hit == 0:
                count += 1
            elif hit == 1:
                score += b3
                b1,b2,b3=1,b1,b2
            elif hit == 2:
                score += b2 + b3
                b1,b2,b3=0,1,b1
            elif hit == 3:
                score += b1 + b2 + b3
                b1,b2,b3 =0,0,1
            elif hit == 4:
                score += b1 + b2 + b3 +1
                b1,b2,b3=0,0,0
            k = (k+1)%9 
    if sm <= score:
        sm = score
print(sm)
