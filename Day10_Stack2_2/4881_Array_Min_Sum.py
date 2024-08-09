import sys
sys.stdin=open('4881_input.txt', 'r')


def permutation(arr, l):
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used):
        if len(chosen) == l:
            result.append(chosen[:])
            return

        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()

    generate([], used)


for t in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    A = [i for i in range(N)]
    result = []
    permutation(A, N)
    sm = []
    for re in result:
        s = 0
        for x in range(N):
            s += arr[x][re[x]]
        sm.append(s)
    print(f'#{t} {min(sm)}')
