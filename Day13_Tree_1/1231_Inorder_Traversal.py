import sys
sys.stdin = open('1231_input.txt', 'r')


class tree:
    def __init__(self, char, left=0, right=0):
        self.left=int(left)
        self.right=int(right)
        self.char=char

def inorder_traverse(T):
    if T:
        if T.left:inorder_traverse(arr[T.left])
        print(T.char, end='')
        if T.right:inorder_traverse(arr[T.right])

for t in range(1, 11):
    N=int(input())
    arr=[0]*(N+1)
    for n in range(1, N+1):
        node, *inp = input().split()
        if len(inp)==3:
            char, left, right=inp
            arr[int(node)] = tree(char, left, right)
        elif len(inp)==2:
            char, left=inp
            arr[int(node)] = tree(char, left)
        else:
            char=inp[0]
            arr[int(node)]=tree(char)

    print(f'#{t}', end=' ')
    inorder_traverse(arr[1])
    print()