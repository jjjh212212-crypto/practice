import sys
import re
sys.stdin = open("sample_input.txt", "r")
password={(3,2,1,1):0, (2,2,2,1):1, (2,1,2,2):2, (1,4,1,1):3, (1,1,3,2):4, (1,2,3,1):5, (1,1,1,4):6, (1,3,1,2):7, (1,2,1,3):8, (3,1,1,2):9}
HEX_TO_BIN = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}
T=int(input())

x16={'A':10, 'B':11,'C':12, 'D':13, 'E':14, 'F':15}
for t in range(1,T+1):
    N,M=map(int,input().split())
    arr=[input() for _ in range(N)]
    check=[]
    result_int=0
    for i in arr:
        if i.count('0') < M:
            # i=i.strip('0')
            # spilt_chunks=re.split('0{4,}',i)
            # for chunk in spilt_chunks:
            #     if chunk == '163589926345A3003746EDE8B626468':
            #         a,b=map(str,chunk.split('00'))
            #         check.append(a)
            #         check.append(b)
            #     elif chunk == '349BB6EDD88B7A0001E667F9E7E07987861E1819E0678':
            #         a,b=map(str,chunk.split('000'))
            #         check.append(a)
            #         check.append(b)
            #     elif chunk == '163589926345A3003746EDE8B626468':
            #         a,b=map(str,chunk.split('00'))
            #         check.append(a)
            #         check.append(b)
            #     elif chunk == '349BB6EDD88B7A0001E667F9E7E07987861E1819E0678':
            #         a,b=map(str,chunk.split('000'))
            #         check.append(a)
            #         check.append(b)
            #     elif chunk == '376EED18D1AC4580078618799FE1E19F9E07987861878':
            #         a,b=map(str,chunk.split('00'))
            #         check.append(a)
            #         check.append(b)
            #     elif chunk == '462C6A3462DB8D01D8D16F5EBD328C':
            #         a,b=map(str,chunk.split('0'))
            #         check.append(a)
            #         check.append(b)
            #     elif chunk:
            #         check.append(chunk)
                    
    # check=list(set(check))
    # print(check)
    
    # for i in check:
        a=0
        k=0
        print(i)
        for j in range(len(i)-1,-1,-1):
            if i[j] in x16:
                a+=x16[i[j]]*16**k
            else:
                a+=int(i[j])*16**k
            k+=1

        result=[]
        while a != 0:
            result.append(a%2)
            a //=2
        result.reverse()

        while result[-1] == 0:
            result.pop()

        while len(result) % 56 != 0:
            result=[0]+result

        check2=[]
        real_result=[]
        count=0
        c0=0
        c1=0
        for i in range(len(result)):
            before0=c0
            before1=c1
            if result[i] == 0:
                c0+=1
            else:
                c1+=1
            if c0 == 1 and c1 != 0 and before0 == 0:
                check2.append(c1)
                c1=0
                count+=1
            elif c1 == 1 and c0 != 0 and before1 ==0 :
                check2.append(c0)
                c0=0
                count+=1
            if i == len(result)-1:
                check2.append(c1)
                c1=0
                count+=1
            if count == 4:
                count-=4
                real_result.append(password[tuple([i//min(check2) for i in check2])])
                check2=[]
        sm=0
        r=0
        for i in range(8):
            if i % 2==0:
                sm+=3*real_result[i]
            else:
                sm+=real_result[i]
            r+=real_result[i]
        
        if sm % 10 == 0:
            result_int+=r
    print(f'#{t} {result_int}')

    
