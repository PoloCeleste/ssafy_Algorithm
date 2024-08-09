import sys
sys.stdin = open('4875_input.txt', 'r')

dij = [[0,1],[1,0],[0,-1],[-1,0]]

def find_start(ar, n):
    po=[]
    for a in range(n):
        for b in range(n):
            if ar[a][b]==2:
                po=[a, b]
                return po


def maze(ar, n):
    stack=[]
    past=[]
    roop=[-1]
    point=find_start(ar, n)
    while ar[point[0]][point[1]] != 3:
        for di, dj in dij:
            ni, nj=point[0]+di, point[1]+dj
            if ni<0 or nj<0 or ni>=n or nj>=n:continue
            if ar[ni][nj]==1:continue
            if stack and [ni,nj] in stack:continue  # 만약 스택이 안비고 이전이랑 같으면
            roop.append([ni, nj])
        stack.append(point)  # 현위치 추가
        point=roop.pop()  # 다음 이동
        if point==-1:return 0
    return 1

for t in range(1, int(input())+1):
    N = int(input())
    arr=[list(map(int, input())) for _ in range(N)]
    print(f'#{t} {maze(arr, N)}')