import sys
sys.stdin=open('1227_input.txt', 'r')
from collections import deque
N=100
dij=[[0,1],[1,0],[0,-1],[-1,0]]

def find():
    for i in range(N):
        for j in range(N):
            if arr[i][j]==2:return [i,j]

def maze(start, visited, path):
    while 1:
        visited[start[0]][start[1]]=1
        for di, dj in dij:
            ni, nj=di+start[0], dj+start[1]
            if ni<0 or ni>=N or nj<0 or nj>=N:continue
            if arr[ni][nj]==3:return 1
            if arr[ni][nj]==1 or visited[ni][nj]:continue
            path.append([ni,nj])
        if not path:return 0
        start=path.popleft()

for T in range(10):
    t=int(input())
    arr=[list(map(int, input())) for _ in range(N)]
    start=find()
    visited=[[0]*N for _ in range(N)]
    path=deque()
    print(f'#{t} {maze(start, visited, path)}')