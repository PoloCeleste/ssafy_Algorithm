import sys
sys.stdin = open('ex1_input.txt', 'r')
for t in range(1, int(input())+1):
    n = int(input())
    di=[0, 1, 0, -1]
    dj=[1, 0, -1, 0]
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    s_arr=[]
    for i in range(n):
        for j in range(n):
            s=[]
            for k in range(4):
                ni = i+di[k]
                nj = j+dj[k]
                if 0<=ni<n and 0<=nj<n:
                    s.append(abs(arr[ni][nj]-arr[i][j]))
            s_arr.append(sum(s))

    print(f'#{t} {sum(s_arr)}')