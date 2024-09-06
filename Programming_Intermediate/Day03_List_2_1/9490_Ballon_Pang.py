import sys
sys.stdin = open('input1.txt', 'r') # input 값 txt로 받기
for t in range(1, int(input())+1): # 테스트케이스 입력받아 루프
    n,m = map(int, input().split()) # 행, 열 입력받고
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] # 배열 입력받기
    result=[] # 각 요소의 결과 저장용 배열
    for i in range(n): # 행 개수만큼 순회
        for j in range(m): # 열 개수만큼 순회
            s=arr[i][j] # 덧셈용 변수에 현재위치 요소 저장
            for x in range(1, arr[i][j]+1):
                dij = [[0, x], [x, 0], [0, -x], [-x, 0]]
                for di, dj in dij: # 상하좌우 위치 계산
                    ni = i+di # i 방향 계산
                    nj = j+dj # j 방향 계산
                    if 0<=ni<n and 0<=nj<m: # 유효인덱스 판단하여
                        s+=arr[ni][nj] # 상하좌우값 더하기
            result.append(s) # 최종 덧셈값 결과리스트에 추가
    print(f'#{t} {max(result)}') # 결과리스트의 최대값 출력

