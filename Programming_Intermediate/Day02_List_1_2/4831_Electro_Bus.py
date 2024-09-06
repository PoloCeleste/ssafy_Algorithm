for t in range(1, int(input())+1):
    K, N, M = map(int, input().split())
    arr = [0]*(N+1)
    for i in list(map(int, input().split())): arr[i] += 1
    flag, x, result = False, 0, 0
    while x < N+1:
        cnt=0
        for y in range(x+K, x, -1):
            if y == N:
                flag = True
                break
            if y < N+1 and arr[y]==1:
                x=y
                result+=1
                break
            cnt+=1
        if cnt == K: break
        if flag: break
    if flag: print(f'#{t} {result}')
    else: print(f'#{t} 0')