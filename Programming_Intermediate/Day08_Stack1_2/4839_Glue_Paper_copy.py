import sys
sys.stdin = open('4869_input.txt', 'r')

for t in range(1, int(input())+1):
    N = int(input())



#jin ver2
def main(N):
    nums = [0, 1, 3, 5]
    if N < 40:
        return [0, 1, 3, 5][N // 10]
    else:
        return main(N - 30) * 2 + main(N - 20) * 3


for t in range(int(input())): print(f'#{t + 1} {main(int(input()))}')



#jin ver1
def main(N):
    nums = [0, 1, 3, 5]
    M = N // 10

    if M < 4:
        return nums[M]
    else:
        return main(N - 30) * 2 + main(N - 20) * 3


for t in range(int(input())):
    N = int(input())
    print(f'#{t + 1} {main(N)}')

#song ver
def paper(n):
    if n >= 3:
        memo[n] = paper(n - 1) + 2 * paper(n - 2)  # DP(N)= DP(N-1)-2DP(N-2)
    return memo[n]  # N=2 or N=1일 때는 해당값 반환


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 가로의 크기
    N //= 10  # 보기 좋기 N 자르기 N=30 -> 3
    memo = [0] * (N + 1)  # N에 따른 결과 N=index인 곳에 넣기위해 N+1크기에 리스트 생성
    memo[1] = 1  # N=10 일때 1
    memo[2] = 3  # N=30 일때 3
    paper(N)
    print(f'#{tc} {memo[-1]}')