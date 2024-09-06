def reverse(s):
    if len(s) == 0: return s
    else: return reverse(s[1:])+s[0]


for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [[a for a in input()] for _ in range(N)]
    flag = False
    for i in range(N):
        if flag: break
        for j in range(N-M+1):
            sr = ''
            sv = ''
            for k in range(M):
                sr += arr[i][k+j]
                sv += arr[k+j][i]
            if sr == reverse(sr):
                print(f'#{t} {sr}')
                flag = True
                break
            if sv == reverse(sv):
                print(f'#{t} {sv}')
                flag = True
                break
