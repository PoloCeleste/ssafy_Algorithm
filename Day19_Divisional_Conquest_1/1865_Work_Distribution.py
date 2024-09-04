import sys
sys.stdin=open('1865_input.txt', 'r')

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