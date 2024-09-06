for t in range(10):
    N = int(input())
    sarr= list(input())
    stack=[]
    sm=0
    for x in range(1, N):
        if x%2==1:
            sarr[x], sarr[x+1] = sarr[x+1], sarr[x]
    for i in range(N):
        if sarr[i].isdigit():
            stack.append(sarr[i])
        else:
            a=stack.pop()
            b=stack.pop()
            sm=(int(a)+int(b))
            stack.append(sm)
    print(f'#{t+1} {stack.pop()}')