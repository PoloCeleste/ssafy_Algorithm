from time import time


def lomuto_partition(left, right):
    idx = left - 1      # 모든 상황에 대해서 동일하게 코드를 작성
    pivot = arr[right]  # lomuto 방식은 for문으로 처리

    # right 번째 -> pivot, range(l, right) -> right-1
    for next in range(left, right):
        if arr[next] < pivot:
            idx += 1
            arr[idx], arr[next] = arr[next], arr[idx]
    arr[idx+1], arr[right]=arr[right], arr[idx+1]
    return idx+1

def quick_sort(left, right):
    if left < right:
        pibot_index= lomuto_partition(left, right)

        quick_sort(left, pibot_index - 1)
        quick_sort(pibot_index + 1, right)

arr=[3,2,4,6,9,1,8,7,5]
start=time()
quick_sort(0, len(arr)-1)
print(time()-start)
def quick_sort1(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quick_sort1(left) + [pivot] + quick_sort1(right)
q=quick_sort1(arr)
print(q)