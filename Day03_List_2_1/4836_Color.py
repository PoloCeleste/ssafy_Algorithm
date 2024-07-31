import sys
sys.stdin = open('sample_input.txt', 'r') # 파일에서 입력받기

for t in range(1, int(input())+1): # 테스트케이스 루프
    N=int(input()) # 칠할 영역 개수
    re = 0 # 결과값
    arr = [[0]*10 for _ in range(10)] # 0으로 채워진 2차원 10X10 배열 생성
    for n in range(N): # 영역 개수만큼 순회
        info = list(map(int, sys.stdin.readline().split())) # 정보리스트 받기
        for x in range(info[0], info[2]+1): # 칠할 영역 행 순회
            for y in range(info[1], info[3]+1): # 칠할 영역 열 순회
                arr[x][y]+=1 # 칠할 영역의 요소에 +1
    for i in range(10): # 다 칠해진 영역 행 순회
        for j in range(10): # 다 칠해진 영역 열 순회
            if arr[i][j] == 2: # 만약 2번 칠해져서 보라색이 되었다면
                ### 주어진 정보에서 같은 색인 영역은 겹치지 않는다. ###
                ### 중복 고려 안해도 됨. 저 조건이 없고 중복이 발생하면 그거도 고려필 ###
                re += 1 # 결과값 +1
    
    print(f'#{t} {re}') # 최종 출력