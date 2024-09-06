import sys
sys.stdin=open('5178_input.txt', 'r')
class tree:
    def __init__(self, left=0,right=0):
        self.left=left
        self.right=right
        self.d=0
    def data(self, d=0):
        self.d=d

for t in range(1, int(input())+1):
    N, M, L=map(int, input().split())
    arr=[0]*(N+1)
    for n in range(1, N+1):
        if (n*2+1)<=N: arr[n]=tree(n*2, n*2+1)
        elif n*2==N: arr[n]=tree(n*2)
        else: arr[n]=tree()
    for _ in range(M):
        LN, d=map(int, input().split())
        arr[LN].data(d)
    for a in range(N, 0, -1):
        if arr[a].d==0:
            if arr[a].right: arr[a].data(arr[arr[a].left].d+arr[arr[a].right].d)
            else: arr[a].data(arr[arr[a].left].d)

    print(f'#{t} {arr[L].d}')