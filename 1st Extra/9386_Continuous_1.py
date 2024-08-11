import sys
sys.stdin = open('9386_input.txt', 'r')

for t in range(1, int(input()) + 1):
    N = int(input())
    arr = input()
    cnt = []
    s = 0
    for a in arr:
        if a == '0':
            if s != 0:
                cnt.append(s)
                s = 0
        else:
            s += 1
    cnt.append(s)
    print(f'#{t} {max(cnt)}')
