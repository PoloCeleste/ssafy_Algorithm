import sys
n=100
sys.stdin = open('sum_input.txt', 'r')

for t in range(1,11):
    T = int(input())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    
    sum_arr = []
    c, d=[], []
    for i in range(n):
        a, b=[], []
        c.append(arr[i][i])
        d.append(arr[n-i-1][i])
        for j in range(n):
            a.append(arr[i][j])
            b.append(arr[j][i])
        sum_arr.extend([sum(a), sum(b)])
    sum_arr.extend([sum(c), sum(d)])
    print(f'#{T} {max(sum_arr)}')