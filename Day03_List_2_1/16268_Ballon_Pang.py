import sys
sys.stdin = open('input1.txt', 'r') # input 값 txt로 받기
for t in range(1, int(input())+1): # 테스트케이스 입력받아 루프
    n,m = map(int, input().split()) # 행, 열 입력받고
    di=[0, 1, 0, -1] # i 방향으로 더할 값
    dj=[1, 0, -1, 0] # j 방향으로 더할 값
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] # 배열 입력받기
    result=[] # 각 요소의 결과 저장용 배열
    for i in range(n): # 행 개수만큼 순회
        for j in range(m): # 열 개수만큼 순회
            s=arr[i][j] # 덧셈용 변수에 현재위치 요소 저장
            for k in range(4): # 상하좌우 위치 계산
                ni = i+di[k] # i 방향 계산
                nj = j+dj[k] # j 방향 계산
                if 0<=ni<n and 0<=nj<m: # 유효인덱스 판단하여
                    s+=arr[ni][nj] # 상하좌우값 더하기
            result.append(s) # 최종 덧셈값 결과리스트에 추가
	#max_s = 0	# 최대값 변수
    #for x in result:  # 결과리스트 순회하며
    #	if x > max_s : max_s = x  # 최대 합 찾기
    print(f'#{t} {max(result)}') # 결과리스트의 최대값 출력