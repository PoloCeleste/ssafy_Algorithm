import sys
sys.stdin = open('1223_input.txt', 'r')
def is_num(c):
    try:float(c)
    except:return False
    else:return True

def postfix(infix):
    postL=[]
    stack=[]
    prec={
        '*':3,
        '/':3,
        '+':2,
        '-':2,
        '(':1
    }
    for i in infix:
        if is_num(i):postL.append(float(i))
        elif i=='(':stack.append(i)
        elif i==')':
            top=stack.pop()
            while top != '(':
                postL.append(top)
                top=stack.pop()
        else:
            while stack and prec[stack[-1]]>=prec[i]:
                postL.append(stack.pop())
            stack.append(i)
    while stack: postL.append(stack.pop())
    return cal(postL)

def cal(calList):
    cal = []
    for c in calList:
        if is_num(c): cal.append(c)
        else:
            try:
                b = cal.pop()
                a = cal.pop()
                if c == '+': cal.append(a + b)
                if c == '-': cal.append(a - b)
                if c == '*': cal.append(a * b)
                if c == '/': cal.append(a // b)
            except:
                return 'error'
    return int(cal.pop())


for t in range(10):
    N=int(input())
    infix = list(input())
    print(f'#{t+1} {postfix(infix)}')