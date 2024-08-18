for t in range(1, int(input()) + 1):
    print(f'#{t}', end=' ')
    arr = [0] * 5001
    N = int(input())
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B + 1): arr[i] += 1
    for _ in range(int(input())):
        print(arr[int(input())], end=' ')
    print()
