from collections import deque

dij = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
co = deque()
co.append(-1)
for di, dj in dij:
    xi, xj = (0 if a==0 else a-1 if a<0 else a+1 for a in [di, dj])
    co.append([xi, xj])
print(co)
if co[0]==-1:
    co.popleft()
    print(co)