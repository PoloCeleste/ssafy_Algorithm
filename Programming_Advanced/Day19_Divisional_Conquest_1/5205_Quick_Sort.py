def quick_sort(arr):
    if len(arr) <= 1: return arr
    pivot = arr[0]
    left =[]
    right = []
    for i in range(1, len(arr)):
        if arr[i] < pivot: left.append(arr[i])
        else: right.append(arr[i])
    return quick_sort(left) + [pivot] + quick_sort(right)

def tim_sort(arr):
    n = len(arr)
    run_size = 32
    for i in range(0, n, run_size):
        insertion_sort(arr, i, min((i+run_size-1), n-1))
    size = run_size
    while size < n:
        for left in range(0, n, 2*size):
            mid = min(n-1, left+size-1)
            right = min((left+2*size-1), (n-1))
            merge(arr, left, mid, right)
        size = 2*size

def insertion_sort(arr, left, right):
    for i in range(left+1, right+1):
        j = i
        while j > left and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

def merge(arr, left, mid, right):
    left_arr = arr[left:mid+1]
    right_arr = arr[mid+1:right+1]
    i = j = 0
    k = left
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

for t in range(1, int(input())+1):
    N=int(input())
    arr=list(map(int, input().split()))
    print(f'#{t} {quick_sort(arr)[N//2]}')