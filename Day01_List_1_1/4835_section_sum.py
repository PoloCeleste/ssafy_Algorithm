for i in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    mn=10000*M # 나올 수 있는 최대값 = 초기 최소값
    mx=0 # 초기 최대값
    for j in range(N-M+1):
        # 마지막 이웃한 M개가 끝나면 index에러 발생하므로 그 이전에 순회 멈춤
        um=0 # 구간 합 계산
        for k in range(M): # 구간 순회하며
            um+=arr[j+k] # 구간 합 더하기
        if um<mn:mn=um # 최소값 비교
        if um>mx:mx=um # 최대값 비교
    print(f'#{i} {mx-mn}') # 최종 출력