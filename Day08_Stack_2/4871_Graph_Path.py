def shortest_path(graph, source, destination): # sourse : start, destination : end
    stack = [source] # 시작위치 넣기
    visited = set() # 방문한 곳 중복 방지 위해 set 생성
    while stack: # 스택이 차 있는 동안
        vertex = stack.pop() # 스택 맨 위 요소 pop
        if vertex == destination: # 뽑은게 목적지라면
            return 1
        visited.add(vertex) # 뽑은 요소 방문셋과 결과에 넣기
        if vertex not in graph.keys():continue
        for adjacent in graph[vertex]: # 그래프의 요소와 연결된 노드에서
            if adjacent not in visited: # 해당 노드의 값이 방문셋에 없다면
                stack.append(adjacent) # 그 값을 스택에 넣기
    return 0 # 결과 반환


import sys
sys.stdin = open('4871_input.txt', 'r')
for t in range(1, int(input())+1):
    graph={}
    V, E = map(int, input().split())
    for i in range(E):
        A, B = map(int, input().split())
        if A in graph:
            graph[A].append(B)
        else:
            graph[A]=[B]
    Start, End = map(int, input().split())
    print(f'#{t} {shortest_path(graph, Start, End)}')