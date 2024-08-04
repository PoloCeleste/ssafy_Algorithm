n = 10


def check(arr, info):
    for i in range(info[0], info[2] + 1):
        for j in range(info[1], info[3] + 1):
            if arr[i][j] == info[4]: continue
            arr[i][j] = info[4]
    return arr


for t in range(1, int(input()) + 1):
    result = 0
    N = int(input())
    arr_Red = [[0] * n for _ in range(n)]
    arr_Blue = [[0] * n for _ in range(n)]
    result_A = [[0] * n for _ in range(n)]
    for _ in range(N):
        info = list(map(int, input().split()))
        if info[4] == 1:
            arr_Red = check(arr_Red, info)

        if info[4] == 2:
            arr_Blue = check(arr_Blue, info)

    for i in range(n):
        for j in range(n):
            result_A[i][j] = arr_Blue[i][j]+arr_Red[i][j]
            if result_A[i][j]==3: result += 1

    print(f'#{t} {result}')
