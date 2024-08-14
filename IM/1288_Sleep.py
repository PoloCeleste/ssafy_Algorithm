import sys
sys.stdin = open('1288_input.txt', 'r')

for t in range(int(input())):
    N = input()
    if N == '1':
        print(f'#{t+1} 10')
        continue
    l, x, result = set(), 1, 0
    while 1:
        result += 1
        for n in range(int(N), int(N)*x+1, int(N)):
            for y in str(n):
                l.add(int(y))
        if len(l) == 10: break
        x += 1
    print(f'#{t+1} {result*int(N)}')