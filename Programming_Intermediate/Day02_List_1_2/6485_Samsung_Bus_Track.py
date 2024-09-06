for i in range(1, int(input())+1): # 테케 순회
    N=int(input()) # 노선 개수
    arr=[list(map(int, input().split())) for _ in range(N)] # 노선 범위
    P=int(input()) # 정류장 개수
    c=[int(input()) for _ in range(P)] # 정류장 번호
    result={} # 임시 결과
    result_l=[] # 최종 결과 리스트
    for x in range(N): # 노선 개수
        for y in range(arr[x][0], arr[x][1]+1): # 노선 지나는 경로
            if y in result: result[y]+=1
            # 임시 결과 딕셔너리에서 지나는 경로 카운트
            else: result[y]=1
    for a in c: # 카운트 끝나고 정류장 리스트 돌면서
        if a in result: result_l.append(result[a])
        # 그 정류장이 카운트한 정류장이면 해당정류장지나는 노선 카운트 횟수 결과에 저장
        else: result_l.append(0)
        # 카운트 한 정류장이 아니면 0을 결과에 추가

    print(f"#{i}", *result_l)


"""
2
2
1 3
2 5
5
1
2
3
4
5
5
1 4
2 10
13 24
36 50
40 45
5
3
35
44
60
39
"""
