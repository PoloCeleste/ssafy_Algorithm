import sys
sys.stdin = open('5431_input.txt', 'r')

for t in range(1, int(input())+1):
    N, K = map(int, input().split())
    al=[i for i in range(1, N+1)]
    arr=list(map(int, input().split()))
    no=list(set(al) - set(arr))
    print(f'#{t}', end=' ')
    print(*no)