def palindromic(a, N):
    for x in range(2, N):
        for i in range(N-x+1):
            if len(a) == (i+x-1): return a
            if a[i] != a[i+x-1]: continue
            if a[i:i+x] == a[i:i+x][::-1]:
                return palindromic(a[:i]+a[i+x:], N)

import sys
sys.stdin = open('pass_input.txt', 'r')
for t in range(1, 11):
    inp = input()
    N, arr = int(inp.split()[0]), inp.split()[1]
    print(f'#{t} {palindromic(arr, N)}')
