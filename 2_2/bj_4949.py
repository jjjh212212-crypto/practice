while True:
    lst=list(input())
    if lst == ['.']:
        break
    for i in range(len(lst)):
        if lst[i] == '[' or lst[i] == '(' :
            countlc=0
            countrc=0
            countlo=0
            countro=0
            for j in range(i,len(lst)):
                if lst[j] == '[':
                    countlc+=1
                elif lst[j] == ']': 
                    countrc+=1
                if countlc == countrc != 0 and lst[i:j+1].count('(') == lst[i:j+1].count(')'):                        
                    lst[i]='#'
                    lst[j]='#'
                    break

                if lst[j] == '(':
                    countlo+=1
                elif lst[j] == ')':
                    countro+=1
                if countlo == countro != 0 and lst[i:j+1].count('[') == lst[i:j+1].count(']'): 
                    lst[i]='#'
                    lst[j]='#'
                    break
   
    print(lst) 
    if '[' in lst or ']' in lst or '(' in lst or ')' in lst:
        print('no')
    else:
        print('yes')





