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
            if len(cal) == 1: return int(cal.pop())
            elif len(cal) < 2:
                b = cal.pop()
                a = cal.pop()
                if c == '+': cal.append(a + b)
                if c == '-': cal.append(a - b)
                if c == '*': cal.append(a * b)
                if c == '/': cal.append(a // b)


if __name__ == '__main__':
    infix = list(input())
    print(postfix(infix))