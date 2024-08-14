import sys

sys.stdin = open('input.txt')
sc = {1: 0, 0: 1}
if __name__ == '__main__':
    sw = int(input())
    switch = list(map(int, input().split()))
    st = int(input())
    for _ in range(st):
        g, n = map(int, input().split())
        if g == 1:
            for i in range(sw):
                if (i + 1) % n == 0:
                    switch[i] = sc[switch[i]]
        if g == 2:
            switch[n - 1] = sc[switch[n - 1]]
            for j in range(1, sw // 2 + 1):
                if n - j <= 0 or n + j > sw: break
                if switch[n - 1 - j] == switch[n - 1 + j]:
                    switch[n - 1 - j], switch[n - 1 + j] = sc[switch[n - 1 - j]], sc[switch[n - 1 + j]]
                else: break
    if sw <= 20:
        print(*switch)
    else:
        for s in range(sw):
            print(switch[s], end=' ')
            if s < (sw - 1) and (s + 1) % 20 == 0: print()
