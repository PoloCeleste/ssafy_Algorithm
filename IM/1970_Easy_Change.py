import sys

sys.stdin = open('1970_input.txt', 'r')

change = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for t in range(1, int(input()) + 1):
    N = int(input())
    print(f'#{t}')
    cnt = [0] * len(change)
    for i in range(len(change)):
        if N == 0: break
        cnt[i] = N // change[i]
        N %= change[i]
    print(*cnt)
