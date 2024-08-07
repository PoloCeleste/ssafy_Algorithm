import sys
sys.stdin = open('space2_input.txt', 'r')
dij = [[0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1], [-1,0], [-1,1]]

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt=0

    for i in range(N):
        for j in range(M):
            s = 0
            L = arr[i][j]
            for di, dj in dij:
                ni, nj = i+di, j+dj
                if ni<0 or nj<0 or ni>=N or nj>=M: continue
                if arr[ni][nj]<L: s+=1
            if s<4:continue
            cnt+=1
    print(f'#{t} {cnt}')
