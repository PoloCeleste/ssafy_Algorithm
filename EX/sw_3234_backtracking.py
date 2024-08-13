import sys
import math

sys.stdin = open("sample_input (1).txt", "r")
import time
st = time.time()
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))


    def dfs(depth, l_sum, r_sum):
        global result

        # 오른쪽 무게의 총합이 왼쪽에 올라가 있는 무게의 총합보다 커지면 안됨
        if l_sum < r_sum:
            return

        if l_sum >= total_w / 2:
            result += (1 << (N - depth)) * math.factorial(N - depth)
            return

        for i in range(N):
            if visited[i]: continue
            visited[i] = True
            dfs(depth + 1, l_sum + arr[i], r_sum)
            dfs(depth + 1, l_sum, r_sum + arr[i])
            visited[i] = False


    result = 0
    visited = [False] * N
    total_w = sum(arr)

    # 주어진 추를 하나씩 왼쪽에 올려놓고 시작을 함

    # 방법 1 => swea 통과
    for n in range(N):
        visited[n] = True
        dfs(1, arr[n], 0)
        visited[n] = False

    # 방법 2 => swea 시간 초과
    # dfs(0, 0, 0)


    print(f"#{test_case} {result}")

et = time.time()
print(et - st)