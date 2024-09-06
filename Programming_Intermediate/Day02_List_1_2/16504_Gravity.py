def bubble_sort(origin, dump):
    arrn = origin[:]
    for i in range(dump-1, 0, -1):
        for j in range(i):
            if arrn[j] > arrn[j + 1]:
                arrn[j], arrn[j + 1] = arrn[j + 1], arrn[j]
    return arrn


for t in range(1, int(input()) + 1):
    dump = int(input())
    arr = list(map(int, input().split()))
    if dump == 1:
        print(f'#{t} 0')
        continue
    sorted_arr = bubble_sort(arr, dump)
    mx = 0
    for x in arr:
        drop = sorted_arr.index(x) - arr.index(x)
        if mx < drop: mx = drop
    print(arr)
    print(sorted_arr)
    print(f'#{t} {mx}')

# 고정된 상태에서 비교해야 가능
# 버블 정렬은 배열이 계속 바뀌므로 불가
# 새로운 배열 생성하고 기존 배열과 인덱스 비교

# for t in range(1, int(input())+1):
#     N = int(input())
#     arr = list(map(int,input().split()))
#     mx = 0
#     for i in range(N):
#         cnt = 0
#         for j in range(i+1, N):
#             if arr[i] > arr[j]: cnt += 1
#         if mx < cnt: mx = cnt
#     print(f'#{t} {mx}')
