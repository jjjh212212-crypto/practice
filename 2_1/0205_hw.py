for _ in range(1,11):
    t=int(input())
    arr=[list(map(int,input().split())) for _ in range(100)]
    x=arr[-1].index(2)
    i=len(arr)-1
    b=0
    c=0
    while i>0:
        if b%2==0:
            while True:
                row=arr[i]
                if x==99:
                    if c==0:
                        if row[x-1]==0:
                            i-=1
                            continue
                        else:
                            b+=1
                            break
                    else:
                        i-=1
                        c=0
                elif x==0: 
                    if c==0:
                        if row[x+1]==0:
                            i-=1
                            continue
                        else:
                            b+=1
                            break
                    else:
                        i-=1
                        c=0
                        continue
                else:
                    if c==0:
                        if row[x+1]==row[x-1]==0:
                            i-=1
                            continue
                        else:
                            b+=1
                            break
                    else:
                        i-=1
                        c=0
                        continue
        else:
            row=arr[i]
            while True:
                if x==0: 
                    if c==0:
                        x+=1
                        c=1
                        continue
                    else:
                        b-=1
                        break
                elif x==99:
                    if c==0:
                        x-=1
                        c=-1
                        continue
                    else:
                        b-=1
                        break
                else:
                    if row[x+1]==1 and c==0:
                        x+=1
                        c=1
                        continue

                    elif row[x-1]==1 and c==0:
                        x-=1
                        c=-1
                        continue
                    if c==1:
                        if row[x+1]==1:
                            x+=1
                        else:
                            b-=1
                            break
                    if c==-1:
                        if row[x-1]==1:
                            x-=1
                        else:
                            b-=1
                            break


    print(f'#{t} {x}')
        


