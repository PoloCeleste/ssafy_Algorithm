import sys
sys.stdin=open('1865_input.txt', 'r')

# Ver.1  24s
for t in range(1, int(input())+1):
    N=int(input())
    co=[c for c in range(N)]
    arr=[list(map(lambda x:x*0.01, map(int, input().split()))) for _ in range(N)]
    if N==1:
        print(f'#{t} {arr[0][0]*100:.06f}')
        continue
    result=0
    visited=[False]*N

    def multi(a):
        c = 1
        for x in range(len(a)):
            c *= arr[x][a[x]]
        return c * 100

    def f(cur_sub):
        global result
        cal=multi(cur_sub)
        if len(cur_sub)==N:
            result=max(cal,result)
            return
        if cal<result:return
        if cal==0:return

        for i in range(N):
            if visited[i]:continue
            visited[i]=True
            f(cur_sub+[co[i]])
            visited[i]=False

    f([])

    print(f'#{t} {result:.06f}')

# ver.2  6s
for t in range(1, int(input())+1):
    N=int(input())
    arr=[list(map(int, input().split())) for _ in range(N)]
    if N==1:
        print(f'#{t} {arr[0][0]:.06f}')
        continue
    result=0
    visited=[False]*N

    def f(n,cur_mul):
        if cur_mul==0:return
        global result
        t=cur_mul*100
        if n==N:
            result=max(t,result)
            return
        if t<result:return

        for i in range(N):
            if visited[i]:continue
            visited[i]=True
            f(n+1, cur_mul*arr[n][i]/100)
            visited[i]=False

    f(0,1)

    print(f'#{t} {result:.06f}')