def bubble_sort(arr):
    for i in range(len(arr)): #range(len(arr)-1, 0, -1)
        for j in range(len(arr)-1): #range(i)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
 
for i in range(1, 11):
    dump = int(input())
    arr=list(map(int, input().split()))
    arr=bubble_sort(arr)
    for _ in range(dump):
        arr[0]+=1
        arr[-1]-=1
        arr=bubble_sort(arr)
    print(f'#{i} {arr[-1]-arr[0]}')