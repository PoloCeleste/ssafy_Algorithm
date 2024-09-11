from heapq import heappop, heappush

for t in range(1, int(input())+1):
    N=int(input())
    arr=list(map(int,input().split()) for _ in range(N))
    heap=[]
    for i in range(N):
        for j in range(N):
            heappush(heap, (arr[i][j], i, j))
    r=[]
    c=0
    while heap:

