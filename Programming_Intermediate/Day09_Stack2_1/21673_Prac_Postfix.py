def is_num(c):
    try: float(c)
    except: return False
    else: return True
prec={
    '*':3,
    '/':3,
    '+':2,
    '-':2,
    '(':1
}
for t in range(int(input())):
    arr= input()
    stack=[]
    post=[]
    for a in arr:
        if is_num(a):post.append(a)
        else:
            if a=='(':stack.append(a)
            elif a==')':
                top=stack.pop()
                while top != '(':
                    post.append(top)
                    top=stack.pop()
            else:
                while stack and prec[stack[-1]]>=prec[a]:
                    post.append(stack.pop())
                stack.append(a)
    while stack: post.append(stack.pop())
    print(f'#{t+1} {"".join(post)}')