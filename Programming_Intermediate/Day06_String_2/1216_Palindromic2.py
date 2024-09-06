import sys

sys.stdin = open('Palin_input.txt', 'r')


# ver4
def palindromic(a):
    for x in range(100, 0, -1):
        for i in range(N * 2):
            for j in range(N - x + 1):
                if a[i][j:j + x] == a[i][j:j + x][::-1]:
                    return len(a[i][j:j + x])


N = 100
for _ in range(10):
    T = int(input())
    arr = [input() for _ in range(N)]
    arr.extend([''.join([arr[j][i] for j in range(N)]) for i in range(N)])
    print(f'#{T} {palindromic(arr)}')

# ver3
N = 100
for t in range(10):
    T = int(input())
    arr = [input() for _ in range(N)]
    arr.extend([''.join([arr[j][i] for j in range(N)]) for i in range(N)])
    mx, flag = 0, False
    for x in range(100, 0, -1):
        if flag: break
        for i in range(N * 2):
            if flag: break
            for j in range(N - x + 1):
                if arr[i][j:j + x] == arr[i][j:j + x][::-1]:
                    mx = len(arr[i][j:j + x])
                    flag = True
                    break
    print(f'#{T} {mx}')

# ver2
N = 100
for _ in range(10):
    T = int(input())
    arr = [[a for a in input()] for _ in range(N)]
    mx = 0
    for i in range(N):
        for j in range(N):
            for x in range(mx, N - j + 1):
                sr = ''
                sv = ''
                for k in range(x):
                    sr += arr[i][k + j]
                    sv += arr[k + j][i]
                if sr == sr[::-1]:
                    if mx < len(sr):
                        mx = len(sr)
                        break
                if sv == sv[::-1]:
                    if mx < len(sv):
                        mx = len(sv)
                        break

    print(f'#{T} {mx}')


# ver1
def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]


N = 100
for _ in range(10):
    T = int(input())
    arr = [[a for a in input()] for _ in range(N)]
    mx = 0
    for i in range(N):
        for j in range(N):
            for x in range(N - j + 1):
                sr = ''
                sv = ''
                for k in range(x):
                    sr += arr[i][k + j]
                    sv += arr[k + j][i]
                if sr == reverse(sr):
                    mx = max(mx, len(sr))
                if sv == reverse(sv):
                    mx = max(mx, len(sv))

    print(f'#{T} {mx}')

# jeanstar_ver
for t in range(1, 11):
    dummy_input = input()
    grid1 = [input().strip() for _ in range(100)]
    grid2 = [list(grid1[j][i] for j in range(100)) for i in range(100)]
    grid = grid1 + grid2

    M = 1
    for i in range(200):
        k = M + 1
        # i행에서 가장 긴 회문의 길이를 찾기
        while k - M < 3:
            for j in range(100 - k + 1):
                if grid[i][j:j + k] == grid[i][j:j + k][::-1]:
                    M = k
                    break
            k += 1
    print(f'#{dummy_input}', M)
