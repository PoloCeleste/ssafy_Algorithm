import sys

sys.stdin = open('1959_input.txt', 'r')

for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    Narr = list(map(int, input().split()))
    Marr = list(map(int, input().split()))
    if N == M:
        s = 0
        for i in range(N):
            s += Narr[i] * Marr[i]
        print(f'#{t} {s}')
        continue
    X = abs(N - M) + 1
    c = [0] * X
    if N > M:
        for x in range(X):
            s = 0
            for n in range(M):
                s += Narr[n + x] * Marr[n]
            c[x] = s
    if M > N:
        for x in range(X):
            s = 0
            for n in range(N):
                s += Narr[n] * Marr[n + x]
            c[x] = s
    print(f'#{t} {max(c)}')
