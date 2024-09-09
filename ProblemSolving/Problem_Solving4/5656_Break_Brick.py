import sys
sys.stdin=open('5656_input.txt','r')

dij=[[-1,0],[1,0],[0,-1],[0,1]]

def shoot(level, remains, now_arr):
    global min_blocks
    # 구슬을 모두 발사 or 남은 벽돌 0이면 종료
    if level==N or remains==0:
        min_blocks=min(min_blocks,remains)
        return
    for col in range(W):
        # 방법1
        # 1. col 위치에 쏘기 전 상태 복사
        # 2. 원본 리스트의 col위치에 구슬발사
        # 3. level+1번 상태로 이동(다음재귀호출)
        # 4. col위치에 쏘기 전 상태 복구

        # 방법2 (복구시간 너무 오래걸림)
        # 1. col 위치에 쏘기 전 상태를 복사
        # 2. 복사한 리스트의 col위치에 구슬 발사
        # 3. 다음 재귀 호출 시 쏘고 난 상태 같이 넘김

        copy_arr=[row[:] for row in now_arr]

        # col 위치에 구슬 발사
        # 1. 첫번째로 만나는 벽돌 위치 찾기

        row=-1
        for r in range(H):
            if copy_arr[r][col]:
                row=r
                break
        if row==-1:continue
        # 벽돌이 없다면 다음열로 넘어감

        # 2. 벽돌의 값만큼 연쇄적으로 제거
        # 행, 열, 파워
        li=[(row,col,copy_arr[row][col])] # 깨질 벽돌 저장
        now_remains=remains-1
        copy_arr[row][col]=0

        while li:
            r, c, p=li.pop()
            for k in range(1,p):
                for di,dj in dij:
                    nr,nc=r+(di*k),r+(dj*k)

                    if nr<0 or nr>=H or nc<0 or nc>=W:continue
                    if copy_arr[nr][nc]==0:continue
                    li.append((nr, nc, copy_arr[nr][nc]))
                    copy_arr[nr][nc]=0
                    now_remains-=1
        for c in range(W):
            idx=H-1
            for r in range(H-1,-1,-1):
                if copy_arr[r][c]:
                    copy_arr[r][c],copy_arr[idx][c]=copy_arr[idx][c],copy_arr[r][c]#가독성 위해 이와 같이 구현
                    idx-=1
        shoot(level+1,now_remains,copy_arr)

for t in range(1, int(input())+1):
    N,W,H=map(int, input().split())
    # 최소벽돌
    # 현재 벽돌이 다 깨지면 더이상 진행 X
    # 현재 남은 벽돌 수 저장
    arr=[list(map(int,input().split())) for _ in range(N)]
    min_blocks=1e9
    blocks=0

    for row in arr:
        for e in row:
            if e:
                blocks+=1

    shoot(0,blocks,arr)

    print(f'#{t} {min_blocks}')