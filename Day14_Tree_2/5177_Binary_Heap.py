from heapq import heappush
for t in range(1, int(input())+1):
    N=int(input())
    arr=list(map(int, input().split()))
    heap=[]
    for a in arr:
        heappush(heap, a)
    p=N//2
    s=0
    while p>0:
        s+=heap[p-1]
        p//=2
    print(f'#{t} {s}')