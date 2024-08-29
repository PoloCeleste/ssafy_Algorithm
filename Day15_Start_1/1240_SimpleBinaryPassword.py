import sys
sys.stdin=open('1240_input.txt','r')

pw={
    '0001101':0,
    '0011001':1,
    '0010011':2,
    '0111101':3,
    '0100011':4,
    '0110001':5,
    '0101111':6,
    '0111011':7,
    '0110111':8,
    '0001011':9
}


for t in range(1, int(input())+1):
    N,M=map(int, input().split())
    a=[x for x in (input() for _ in range(N)) if '1' in x][0]
    idx=0
    for i in range(M-1,0,-1):
        if a[i]=='1':
            idx=i
            break
    a=a[i-55:i+1]
    pwd=[0]*8
    for i in range(8):
        pwd[i]=a[i*7:(i+1)*7]
        pwd[i]=pw[pwd[i]]
    chksum=sum(pwd[p] for p in range(8) if p%2==0)*3+sum(pwd[p] for p in range(8) if p%2==1)
    if chksum%10==0: print(f'#{t} {sum(pwd)}')
    else:print(f'#{t} 0')


