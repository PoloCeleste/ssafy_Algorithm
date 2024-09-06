for t in range(1, int(input()) + 1):
    A, B = input().split()
    cnt = p = c = 0
    while c < len(A):
        cnt += 1
        if A[c] != B[p]:
            c = c - p + 1
            p = 0
            continue
        p += 1
        c += 1

        if p == len(B):
            p = 0
            c = c - p + 1
            cnt -= len(B)
        print(cnt)
    print(f'#{t} {cnt}')
