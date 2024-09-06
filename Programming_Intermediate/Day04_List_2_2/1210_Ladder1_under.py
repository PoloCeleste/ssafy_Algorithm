import sys

n=100 # 행/열 크기
# di=[0, 0, -1] # 행 탐색할 위치
# dj=[1, -1, 0] # 열 탐색할 위치
dij = [[0, 1], [0, -1], [-1, 0]]

# def search(ladder, point, pre): # 경로 탐색 함수
#     for k in range(3): # 위를 제외한 좌우 아래 탐색
#         ni = point[0]+di[k] # 탐색할 행 인덱스
#         nj = point[1]+dj[k] # 탐색할 열 인덱스
#         if [ni, nj]==pre: # 만약 이전 위치와 같다면
#             continue
#         if 0<=ni<n and 0<=nj<n: # 만약 탐색 위치가 인덱스 범위 안이면
#             if ladder[ni][nj]==1: # 경로 확인해보고 만약 갈 수 있다면
#                 pre, point = point, [ni, nj] # 이전값과 현재값 갱신하여
#                 return point, pre # flag값과 함께 반환

# def find_destination(ladder): # 목적지 찾기 함수
#     for x in range(n): # 열 크기만큼 순회하며
#         if ladder[99][x] == 2: # 0행 x열이 시작지이면
#             point = [99, x] # 초기 탐색포인트 설정
#             pre = [99, x] # 초기 이전포인트 설정
#             for _ in range(n*10): # 루프 돌면서
#                 try: # 경로 탐색 시도
#                     point, pre = search(ladder, point, pre) # 경로 탐색
#                 except TypeError: # 만약 한개의 경로 탐색 완료되어 반환 값이 없다면
#                     return point[1] # 현재 시작지 반환하고 함수 종료
#     return False # 탐색 돌면서 아무것도 발견 못하면 False 반환

def search(ladder, point):
    for di, dj in dij:
        ni, nj = point[0]+di, point[1]+dj
        if 0<=ni<n and 0<=nj<n and ladder[ni][nj]==1:
            ladder[ni][nj]=0
            return [ni, nj]

def find_destination(ladder):
    x=ladder[n-1].index(2)
    point = [n-1, x]
    while point[0] != 0:
        point= search(ladder, point)
    return point[1]

if __name__ == '__main__':
    sys.stdin=open('ladder_input.txt', 'r') # 파일 읽기설정
    for _ in range(10): # 테스트케이스 10회 반복
        T=int(input()) # 테스트케이스
        ladder = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] #게임판 입력받기
        
        print(f'#{T} {find_destination(ladder)}') #경로 탐색하여 결과 출력