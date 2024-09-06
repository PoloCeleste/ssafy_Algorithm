def hoare_partition(left, right):
    pivot = arr[left]
    left+=1
    while True:
        # left index가 right index보다 작고
        while left <= right and arr[left] < pivot:
            # 그 left  번째 값이 pivot보다 작다면,
            left+=1
        while left <= right and arr[right] > pivot:
            right-=1
        if left >= right:
            return right # 피봇 인덱스로 사용
        arr[left], arr[right] = arr[right], arr[left]
# left : 왼쪽 정렬 대상 시작지점
# right : 오른쪽 정렬 대상 시작지점

def quick_sort(left, right):
    if left >= right: return
    # 호어 파티션 구분 결과로 인덱스 얻기
    pivot_index=hoare_partition(left, right)
    arr[left], arr[pivot_index] = arr[pivot_index], arr[left]

    quick_sort(left, pivot_index - 1)
    quick_sort(pivot_index + 1, right)

arr=[3,2,4,6,9,1,8,7,5]
quick_sort(0, len(arr)-1)