from collections import deque
import sys
sys.stdin = open('4615_input.txt', 'r')
dij=[[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
o={1:2,2:1}
for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(N)]
    xy = [[0,-1],[-1,-1],[-1,0]]
    for x, y in xy: arr[N//2+x][N//2+y]=-(x+y)
    arr[N//2][N//2]=2

    for _ in range(M):
        j, i, c = map(int, input().split())
        arr[i-1][j-1]=c
        for di, dj in dij:
            ni, nj = i-1+di, j-1+dj
            if ni<0 or nj<0 or ni>=N or nj>=N: continue
            if arr[ni][nj]==c: continue
            if arr[ni][nj]==0: continue
            change=deque()
            change.append(-1)
            change.append([ni, nj])
            for k in range(1, N):
                yi, yj = i-1 + di*k, j-1 + dj*k
                if yi < 0 or yj < 0 or yi >= N or yj >= N: break
                if arr[yi][yj]==0:break
                if arr[yi][yj]==c:
                    change.popleft()
                    break
                change.append([yi,yj])
            if change[0]==-1: continue
            for x, y in change: arr[x][y]=c
    print(f'#{t} {sum(a.count(1) for a in arr)} {sum(a.count(2) for a in arr)}')