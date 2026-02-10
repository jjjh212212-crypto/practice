while True:
    lst=list(input())
    if lst == ['.']:
        break
    for i in range(len(lst)):
        if lst[i] == '(' or lst[i] == '[':
            for j in range(len(lst)-1,i,-1):
                if lst[j] == ')' and lst[i]=='(':
                    if  lst[i:j+1].count('[') != lst[i:j+1].count(']'):
                        break
                    else:
                        for k in range(i,j+1):
                            if lst[k] == ')' and '(' not in lst[i:k]:
                                lst[i]='#'
                                lst[k]='#'
                                break
                            else:
                                lst[i]='#'
                                lst[j]='#'
                                break
                    if lst[i]=='#':
                        break
                if lst[j] == ']' and lst[i]=='[':
                    if lst[i:j+1].count('(') != lst[i:j+1].count(')'):
                        break
                    else:
                        for k in range(i,j+1):
                            if lst[k] == ']' and '[' not in lst[i:k]:
                                lst[i]='#'
                                lst[k]='#'
                                break
                            else
                                :
                                lst[i]='#'
                                lst[j]='#'
                                break
                    if lst[i]=='#':
                        break
    print(lst)
    if '(' in lst or '[' in lst or ']' in lst or ')' in lst:
        print('no')
    else:
        print('yes')