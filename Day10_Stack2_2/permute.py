# def permute(array, length):
#     result = []
#
#     def backtrack(first=0):
#         if first == length:
#             result.append(array[:])
#         for i in range(first, length):
#             array[first], array[i] = array[i], array[first]
#             backtrack(first + 1)
#             array[first], array[i] = array[i], array[first]
#
#     backtrack()
#     return result
#
#
# print(permute([1, 2, 3, 4], 3))

def permutation(arr, l, result):
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used):
        if len(chosen) == l:
            result.append(chosen[:])
            return

        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()

    generate([], used)
    return result

if __name__ == '__main__':
    results=permutation([1,2,3,4],3,[])
    print(results)