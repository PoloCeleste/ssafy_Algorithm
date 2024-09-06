import sys
sys.stdin = open('Sudoku_input.txt', 'r')
sorted_arr = [1,2,3,4,5,6,7,8,9] # 비교할 정렬된 리스트
di=[0,1,1,1,0,-1,-1,-1]  # i 방향으로 더할 값
dj=[1,1,0,-1,-1,-1,0,1]  # j 방향으로 더할 값
n = 9 # 배열 행,열 길이

for t in range(1,int(input())+1): # 입력받은 테스트 케이스만큼 루프
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] # 배열 입력받기

    result = 0 #스도쿠 검증 결과 횟수
    r=0 # 최종 출력결과
    
    for i in range(n): # 행 순회
        a, b=[], [] # 행, 열 요소 확인용 리스트
        
        for j in range(n): # 열 순회
            a.append(arr[i][j]) # 행 우선탐색
            b.append(arr[j][i]) # 열 우선탐색
            
            # 만약 스도쿠 퍼즐 각 구역의 가운데 위치면
            if (i-1)%3==0 and (j-1)%3==0:
                s=[arr[i][j]] # 구역 요소 확인용 리스트에 현재위치 요소 넣고
                
                for k in range(8): # 8방위로 탐색 순회
                    ni = i+di[k] # i 방향 계산
                    nj = j+dj[k] # j 방향 계산
                    # 구역 가운데이므로 인덱스는 범위를 벗어날 일 없으므로 바로 추가                
                    s.append(arr[ni][nj])
                    
                # 최종 생성/정렬된 구역요소리스트가 비교용리스트와 같으면
                if sorted_arr == sorted(s):
                    result+=1 # 검증결과 +1
                    
        # 대각선의 요소를 공유하는 정렬된 행과 열이 비교용 리스트와 같으면 
        if sorted(a) == sorted(b) == sorted_arr :
            result+=1 # 검증결과 +1
            
    # 만약 검증결과가 모두 맞으면(18회) 출력값 1로 저장
    if result == 18 : r = 1
        
    print(f'#{t} {r}') # 최종결과 출력