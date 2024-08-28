import sys
sys.stdin = open('1232_input.txt', 'r')

class tree:
    def __init__(self, char, left=0, right=0):
        self.left=int(left)
        self.right=int(right)
        self.char=char

def is_num(c):
    try:float(c)
    except:return False
    else:return True

def postorder_traverse(T):
    l=r=0.0
    if T:
        if T.left:
            postorder_traverse(arr[T.left])
            l=arr[T.left].char
        if T.right:
            postorder_traverse(arr[T.right])
            r=arr[T.right].char
        if is_num(l) and is_num(r):
            if T.char=='+':T.char=float(l)+float(r)
            elif T.char=='-':T.char=float(l)-float(r)
            elif T.char=='*':T.char=float(l)*float(r)
            elif T.char=='/':T.char=float(l)/float(r)

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

    postorder_traverse(arr[1])
    print(f'#{t} {int(arr[1].char)}')


"""
def postorder_traverse(T):
    if T:
        if T.left:postorder_traverse(arr[T.left])
        if T.right:postorder_traverse(arr[T.right])
        result.append(T.char)

for t in range(1, 11):
    N=int(input())
    arr=[0]*(N+1)
    result=[]
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

    postorder_traverse(arr[1])

    cal=[]
    for r in result:
        if is_num(r):cal.append(float(r))
        else:
            b=cal.pop()
            a=cal.pop()
            if r=='+':cal.append(a+b)
            elif r=='-':cal.append(a-b)
            elif r=='*':cal.append(a*b)
            elif r=='/':cal.append(a/b)
    print(f'#{t} {int(cal.pop())}')
"""