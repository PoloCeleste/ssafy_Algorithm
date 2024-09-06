for i in range(1, int(input())+1):
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        if i%3==0 and i>10 and i%10!=0:
            print('--', end=' ')
        else: print('-', end=' ')
    else : print(i, end=' ')