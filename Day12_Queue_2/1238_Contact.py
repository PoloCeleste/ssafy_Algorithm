import sys
sys.stdin=open('1238_input.txt', 'r')
from collections import deque
def f(s):
    q=deque([s])
    contact[s]=0
    while q:
        n=q.popleft()
        if n not in graph:continue
        for p in graph[n]:
            if contact[p]!=-1:continue
            q.append(p)
            contact[p]=contact[n]+1

for t in range(1,11):
    N, s=map(int, input().split())
    arr=list(map(int, input().split()))
    graph={}
    contact=[-1]*101
    for i in range(0,N,2):
        if arr[i] not in graph: graph[arr[i]]=set()
        graph[arr[i]].add(arr[i+1])

    f(s)
    mx,mx_d=0,0
    for i in range(1,101):
        if mx_d<=contact[i]:mx,mx_d=i,contact[i]
    print(f'#{t} {mx}')
