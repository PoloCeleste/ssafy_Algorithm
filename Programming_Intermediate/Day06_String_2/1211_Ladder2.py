import sys
import copy

n = 100  # 행/열 크기
dij = [[0, 1], [0, -1], [1, 0]]  # 탐색할 좌표


def search(arr, point):  # 주변칸 탐색
    for di, dj in dij:  # 좌표 리스트 돌면서
        ni, nj = point[0] + di, point[1] + dj  # 탐색할 좌표 설정하고
        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 1:  # 그 좌표가 인덱스 범위 안이면서 값이 1이면
            arr[ni][nj] = 0  # 그 값을 0으로 바꾸고
            return [ni, nj]  # 그 좌표 반환


def find_destination(origin):  # 목적지 찾기 함수
    mn, xin = (n * n), 0  # 최소값 찾기용
    for x in range(n):  # 열 크기만큼 순회하며
        if origin[0][x] == 0: continue  # 시작지가 0이면 다음 x로 이동
        point, c = [0, x], 0  # 1이라면 초기 탐색포인트와 count 초기값 설정
        arr = copy.deepcopy(origin)  # 길찾기용 배열 생성
        while point[0] != 99:  # x 좌표가 99가 될때까지 루프돌며
            c += 1  # 경로 탐색 길이 +1
            point = search(arr, point)  # 경로 탐색
        if c < mn: mn, xin = c, x  # 최종적으로 찾은 경로가 최소값보다 작으면 그 값과 x 좌표 저장
    return xin  # 최종적으로 찾은 x좌표 반환


if __name__ == '__main__':
    sys.stdin = open('ladder2_input.txt', 'r')
    for _ in range(10):
        T = int(input())
        ladder = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
        print(f'#{T} {find_destination(ladder)}')
