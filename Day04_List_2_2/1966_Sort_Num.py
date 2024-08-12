def bubble(arr, N):
    for i in range(N):
        for j in range(N-1):
            if arr[j]>arr[j+1]: arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

for t in range(1, int(input())+1):
    N=int(input())
    arr=list(map(int, input().split()))
    arr=bubble(arr, N)
    print(f'#{t}', end=' ')
    print(*arr)