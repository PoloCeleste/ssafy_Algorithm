T = int(input())
for i in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    mn=arr[0]
    mx=arr[0]
    for j in range(N):
        if arr[j]<mn:mn=arr[j]
        if arr[j]>mx:mx=arr[j]
    print(f'#{i} {mx-mn}')