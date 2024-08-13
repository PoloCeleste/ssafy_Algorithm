import sys
sys.stdin = open('5099_input.txt', 'r')

for t in range(int(input())):  # 테스트 케이스 반복
    N, M = map(int, input().split())  #  N:화덕 크기, M:피자 개수
    arr = list(map(int, input().split()))  # 각 피자 위 치즈 양
    c=[k for k in range(N)]  # 최초 화덕 내 피자 위치(인덱스)
    y=0  # 피자 위치 계산
    while 1:  # 반복
        x=c.pop(0)  # 1번 위치 pop
        arr[x]//=2  # 해당 위치의 피자 치즈양 // 2
        if arr.count(0)==M-1:break
        if arr[x]==0:
            if N+y<M:
                c.append(N+y)
                y+=1
            else:c.append(x)
        else:c.append(x)
    for a in range(M):
        if arr[a]!=0:
            y=a+1
            break
    print(f'#{t+1} {y}')

    """
    b, p = arr[:N], arr[N:]  # 최초 화덕에 들어간 피자 / 남은 피자
    c = [i for i in range(1, N+1)]  # 최초 화덕에 들어간 피자 위치(1부터 시작)
    Flag, x = True, 1
    while Flag:
        for i in range(N):
            b[i] //= 2
            if b.count(0) == (N-1):
                Flag = False
                break
            if b[i] == 0:
                if p:
                    b[i], c[i] = p.pop(0), N+x
                    x += 1
    print(f'#{t+1} {c[b.index(1)]}')"""
