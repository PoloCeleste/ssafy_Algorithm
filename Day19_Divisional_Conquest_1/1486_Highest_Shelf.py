import sys
sys.stdin=open('1486_input.txt')

for t in range(1, int(input())+1):
    N, B=map(int, input().split())
    arr=list(map(int, input().split()))
    if N==1: print(f'#{t} 0'); continue;
    c=10000*N
    def f(n, s):
        global c
        if s>=c:return
        if n==N:
            if s>=B: c=min(c,s)
            return
        f(n+1, s+arr[n])
        f(n+1, s)
    f(0,0)
    print(f'#{t} {c-B}')