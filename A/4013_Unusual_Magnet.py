import sys
sys.stdin=open('4013_input.txt','r')

def rot():
    n, r = map(int, input().split())
    n-=1
    mag=[False]*4
    mag[n]=True
    def check(a,i):
        if a<0 or a>=4:return
        if i>3:return
        if not mag[a]:return
        if a-1>=0:
            if arr[a][6]!=arr[a-1][2]:
                mag[a-1]=True
            check(a-1,i+1)
        if a+1<4:
            if arr[a][2]!=arr[a+1][6]:
                mag[a+1]=True
            check(a+1,i+1)
    check(n,1)
    dir=[0]*4
    dir[n]=r
    for i in range(1,4):
        if i%2==0:
            if n-i>=0:dir[n-i]=dir[n]
            if n+i<4:dir[n+i]=dir[n]
        else:
            if n-i>=0:dir[n-i]=-dir[n]
            if n+i<4:dir[n+i]=-dir[n]
    for x in range(4):
        if mag[x]:
            if dir[x]==1:arr[x]=[arr[x].pop()]+arr[x]
            else:arr[x]=arr[x]+[arr[x].pop(0)]

for t in range(1, int(input())+1):
    K=int(input())
    arr=[list(map(int,input().split())) for _ in range(4)]
    for _ in range(K):rot()
    print(f'#{t} {sum(arr[i][0]*(2**i) for i in range(4))}')