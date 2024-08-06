def palindromic(a, N):
    if len(a)==1: return 1
    for i in range(N-1):
        if len(a) == (i+1): return len(a)
        if a[i] != a[i+1]: continue
        if a[i:i+2] == a[i:i+2][::-1]:
            return palindromic(a[:i]+a[i+2:], N)

import sys
sys.stdin = open('rm_input.txt', 'r')
for t in range(1, int(input())+1):
    arr = input()
    print(f'#{t} {palindromic(arr, len(arr))}')