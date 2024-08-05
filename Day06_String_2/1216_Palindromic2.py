N = 100
for t in range(1, 11):
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

    print(f'#{t} {mx}')