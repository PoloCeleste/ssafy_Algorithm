def search(n):
    if n:
        global cnt
        cnt += 1
        search(tree[n][0])
        search(tree[n][1])


for t in range(1, int(input()) + 1):  # 테케 반복
    E, N = map(int, input().split())  # 간선 개수, 탐색 시작 노드
    tree = [[0, 0] for _ in range(E + 2)]  # 노드 개수 == 간선 개수 + 1, 노드 번호 1부터 시작
    arr = list(map(int, input().split()))  # 부모-자식 조합 받기
    cnt = 0  # 서브트리 노드 카운트
    for i in range(len(arr) // 2):
        p = arr[i * 2]  # 부모
        s = arr[i * 2 + 1]  # 자식
        if not tree[p][0]:
            tree[p][0] = s  # 왼쪽 비어있으면 왼쪽에 넣기
        else:
            tree[p][1] = s  # 왼쪽 차있으면 오른쪽에 넣기
    search(N)  # 서브트리 노드 탐색
    print(f'#{t} {cnt}')  # 결과 출력

"""
3
5 1
2 1 2 5 1 6 5 3 6 4
5 1
2 6 6 4 6 5 4 1 5 3
10 5
7 6 7 4 6 9 4 11 9 5 11 8 5 3 5 2 8 1 8 10
"""
"""
#1 3
#2 1
#3 3
"""