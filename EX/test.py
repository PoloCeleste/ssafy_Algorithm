from math import factorial
import sys
from time import time

sys.stdin = open("sample_input (1).txt", "r")
def dfs(depth, l_sum, r_sum, result):
        r = result
        if l_sum < r_sum: return r
        if l_sum >= total_w / 2:
            r += (1 << (N - depth)) * factorial(N - depth)
            return r
        for i in range(N):
            if visited[i]: continue
            visited[i] = 1
            r = dfs(depth + 1, l_sum + arr[i], r_sum, r)
            r = dfs(depth + 1, l_sum, r_sum + arr[i], r)
            visited[i] = 0
        return r
if __name__ == '__main__': 
    for test_case in range(1, int(input())+1):
        N = int(input())
        arr = list(map(int, input().split()))
        result = 0
        visited = [0] * N
        total_w = sum(arr)
        st = time()
        for n in range(N):
            visited[n] = 1
            result = dfs(1, arr[n], 0, result)
            visited[n] = 0
        print(time()-st)
        print(f"#{test_case} {result}")