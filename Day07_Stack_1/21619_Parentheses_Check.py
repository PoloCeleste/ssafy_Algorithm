import sys
sys.stdin = open('bracket_input.txt', 'r')

for t in range(1, int(input()) + 1):
    paren = input()
    cnt = []
    if paren[0] == ')':
        print(f'#{t} -1')
        continue
    for p in paren:
        if p == '(': cnt.append(1)
        if p == ')': cnt.pop()
    if len(cnt) == 0:
        print(f'#{t} 1')
    else:
        print(f'#{t} -1')
