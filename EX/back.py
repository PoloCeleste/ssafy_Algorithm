import sys

sys.stdin = open('input.txt')
sc = {1: 0, 0: 1}  # 스위치 바꾸기용
if __name__ == '__main__':
    sw = int(input())  # 스위치 개수
    switch = list(map(int, input().split()))  # 스위치 초기 상태
    st = int(input())  # 사람 수
    for _ in range(st):  # 사람 수만큼 루프돌면서
        g, n = map(int, input().split())  # 성별, 스위치 번호(1부터 시작) 순
        if g == 1:  # 남자이면
            for i in range(sw):  # 스위치 개수루프
                if (i + 1) % n == 0: switch[i] = sc[switch[i]]  # i+1이 스위치 번호의 배수일 때(번호 1부터 시작) 상태 변경
        if g == 2:  # 여자이면
            switch[n - 1] = sc[switch[n - 1]]  # 받은 스위치 번호 위치의 상태 변경 먼저 하고
            for j in range(1, sw // 2 + 1):  # 받은 위치 제외하고 스위치 개수의 절반만큼 루프 돌면서
                if n - j <= 0 or n + j > sw: break  # 만약 스위치 범위 벗어나면 종료
                if switch[n-1-j] != switch[n-1+j]: break  # 좌우 스위치 상태가 같지 않아도 종료
                switch[n-1-j], switch[n-1+j] = sc[switch[n-1-j]], sc[switch[n-1+j]]  # j만큼 이동한 좌우 스위치 상태 변경
    if sw <= 20: print(*switch)   # 출력 값이 20개 이하면 언패킹으로 바로 출력
    else:  # 20개 이상이면
        for s in range(sw):  # 스위치 개수만큼 루프 돌면서
            print(switch[s], end=' ')  # end를 공백문자로 하여 스위치 상태 각각 출력
            if s < (sw - 1) and (s + 1) % 20 == 0: print()  # 만약 현 위치가 20개로 나눠떨어지면서 다음 스위치가 존재할 때 줄바꿈
