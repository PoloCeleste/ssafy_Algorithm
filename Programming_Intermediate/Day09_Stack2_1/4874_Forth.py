import sys
sys.stdin = open('4874_input.txt', 'r')

def is_num(s):
    try: float(s)
    except: return False
    else: return True

def cal(calList):
    cal = []
    for c in calList:
        if is_num(c):
            cal.append(float(c))
        elif c == '.':
            if len(cal)==1: return int(cal.pop())
            else: return 'error'
        else:
            if len(cal) < 2:
                b = cal.pop()
                a = cal.pop()
                if c == '+': cal.append(a + b)
                if c == '-': cal.append(a - b)
                if c == '*': cal.append(a * b)
                if c == '/': cal.append(a // b)
            else: return 'error'


for t in range(1, int(input())+1):
    calL=input().split()
    print(f'#{t} {cal(calL)}')