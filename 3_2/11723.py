import sys
input = sys.stdin.readline
N=int(input().strip())
S=set()
for _ in range(N):
    st=input().strip()
    if ' ' in st:
        st,num = st.split()
        num = int(num)
    if st == 'add':
        S.add(num)
    elif st == 'remove':
        if num in S:
            S.remove(num)
    elif st == 'check':
        if num in S:
            print(1)
        else:
            print(0)
    elif st == 'toggle':
        if num in S:
            S.remove(num)
        else:
            S.add(num)
    elif st == 'all':
        S = {i for i in range(1,21)}
    elif st == 'empty':
        S = set()

