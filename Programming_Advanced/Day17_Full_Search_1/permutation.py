def permute(acc, arr):
    if len(arr) == 0:
        result.append(acc)
        return
    for i in range(len(arr)):
        next_element = arr[i]
        arr[i], arr[-1] = arr[-1], arr[i]
        permute(acc + [next_element], arr[:-1])
        arr[i], arr[-1] = arr[-1], arr[i]


result = []
arr = [1, 2, 3]
permute([], arr)
print(result)
