def DFS(graph, start):
    visited = set()
    stack = [start]
    result = []
    visited.add(start)
    v = start
    result.append(start)
    while 1:
        for w in graph[v]:
            if w in visited: continue
            stack.append(w)
            result.append(w)
            visited.add(w)
            v = w
            break
        else:
            if stack:
                v = stack.pop()
            else:
                break
    return result


if __name__ == '__main__':
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))
    gr = {}
    for i in range(E):
        if arr[i * 2] in gr:
            gr[arr[i * 2]].append(arr[i * 2 + 1])
        else:
            gr[arr[i * 2]] = [arr[i * 2 + 1]]
        if arr[i * 2 + 1] in gr:
            gr[arr[i * 2 + 1]].append(arr[i * 2])
        else:
            gr[arr[i * 2 + 1]] = [arr[i * 2]]
    print('#1', end=' ')
    print(*DFS(gr, 1), sep='-')

# input :
# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

#수업
# def DFS(s, V):            # s 시작 정점, V 정점 개수(1번부터인 정점의 마지막 정점)
#     visited = [0]*(V+1)   # 방문한 정점을 표시
#     stack = []            # 스택 생성
#     result = []
#     visited[s] = 1        # 시작정점 방문 표시
#     v = s
#     result.append(str(v))
#     while True:
#         for w in adjL[v]:   # v에 인접하고 방문 안 한 w가 있으면,
#             if visited[w] == 0:
#                 stack.append(v)     # push(v) 현재 정점을 push하고
#                 v = w               # w에 방문
#                 visited[w] = 1      # w에 방문 표시
#                 result.append(str(v))
#                 break               # v부터 다시 탐색
#         else:                       # 남은 인접 정점이 없어서 break가 걸리지 않은 경우
#             if stack:               # 이전 갈림길을 스택에서 꺼내서 ... if TOP > -1
#                 v = stack.pop()
#             else:       # 되돌아갈 곳이 없으면 남은 갈림길이 없으면 탐색 종료
#                 break   # while True:
#     return result

# if __name__ == '__main__':
#     V, E = map(int, input().split())
#     adjL = [[] for _ in range(V+1)]
#     arr = list(map(int, input().split()))
#     for i in range(E):
#         v1, v2 = arr[i*2], arr[i*2+1]
#         adjL[v1].append(v2)
#         adjL[v2].append(v1)

#     print('#1', end=' ')
#     print(*DFS(1, V), sep='-')

