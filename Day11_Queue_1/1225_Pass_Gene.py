import sys
sys.stdin = open('1225_input.txt', 'r')
for t in range(10):
    T = int(input())
    arr = list(map(int, input().split()))
    i = 1
    while 1:
        x = arr.pop(0)-i
        if x <= 0:
            arr.append(0)
            break
        arr.append(x)
        i = i % 5 + 1

    print(f'#{T}')
    print(*arr)
