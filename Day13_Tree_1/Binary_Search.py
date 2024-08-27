class tree:
    def __init__(self, left=0, right=0):
        self.left=left
        self.right=right
    def data(self, data):
        self.data=data
    def __str__(self):
        return f'\n data:{self.data} left:{self.left} right:{self.right}\n'

def inorder(N):
    if arr[N]:
        global cnt
        if arr[N].left:inorder(arr[N].left)
        arr[N].data(cnt)
        cnt+=1
        if arr[N].right:inorder(arr[N].right)

for t in range(1, int(input())+1):
    X=int(input())
    cnt=1
    arr=[0]*(X+1)
    for i in range(1,X+1):
        if (i*2+1)<=X:
            arr[i]=tree(i*2, i*2+1)
        elif (i*2)==X:
            arr[i]=tree(i*2)
        else: arr[i]=tree()
    inorder(1)
    print(f'#{t} {arr[1].data} {arr[X//2].data}')