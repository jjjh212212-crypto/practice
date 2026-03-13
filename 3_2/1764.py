import sys
input = sys.stdin.readline

N, M = map(int, input().split())

set_hear = set()
for _ in range(N):
    # .add()를 사용하면 기존 집합을 복사하지 않고 원소만 추가합니다.
    set_hear.add(input().strip())

set_see = set()
for _ in range(M):
    set_see.add(input().strip())

# 교집합 연산 (이건 매우 효율적입니다!)
set_hs = set_hear & set_see

# 사전 순 출력을 위해 리스트로 변환 후 정렬
result = sorted(list(set_hs))

print(len(result))
for name in result:
    print(name)
# import sys
# input=sys.stdin.readline
# N,M = map(int,input().strip().split())
# set_hear=set()
# set_see=set()
# for _ in range(N):
#     set_hear=set_hear | set((input().strip(),))
# for _ in range(M):
#     set_see= set_see | set((input().strip(),))
# set_hs=set_hear&set_see
# s=len(set_hs)
# print(s)
# for i in set_hs:
#     print(i)
# result=[]
# count=0
# for _ in range(M):
#     a=input().strip()
#     if a in set_hear:
#         count+=1
#         result.append(a)
# print(count)
# result.sort()
# for i in result:
#     print(i)