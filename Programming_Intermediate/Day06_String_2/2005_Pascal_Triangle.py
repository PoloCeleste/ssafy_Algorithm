import sys
sys.stdin = open('pascal_input.txt', 'r')

for t in range(1, int(input())+1):
    N = int(input())
    print(f'#{t}')
    arr=[[1]]
    for i in range(1, N):
        tmp = [0]*(i+1)
        for j in range(i+1):
            c = 0
            if j-1>=0: c += arr[i-1][j-1]
            if j<=(i-1): c += arr[i-1][j]
            tmp[j]=c
        arr.append(tmp)

    for a in arr:
        print(*a)