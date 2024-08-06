import sys

sys.stdin = open('pa_input.txt', 'r')
for t in range(1, int(input()) + 1):
    string = input()
    rs = []
    result = 1
    for s in string:
        if s == '(' or s == '{':
            rs.append(s)
            continue
        if s == ')':
            try:
                if ord(s) - ord(rs.pop()) == 1: continue
            except IndexError:
                result = 0
                break
            result = 0
            break
        if s == '}':
            try:
                if ord(s) - ord(rs.pop()) == 2: continue
            except IndexError:
                result = 0
                break
            result = 0
            break
    if len(rs): result = 0
    print(f'#{t} {result}')
