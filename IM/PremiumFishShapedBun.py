import sys
sys.stdin = open('1860_input.txt','r')

for t in range(1,int(input())+1):
    N,M,K=map(int,input().split())
    a=sorted(list(map(int,input().split())))
    if a[0]<M:
        print(f'#{t} Impossible')
        continue
    r=True
    for i in range(N):
        if ((a[i]//M)*K-(i+1))<0:
            r=False
            break
    if r:print(f'#{t} Possible')
    else:print(f'#{t} Impossible')


