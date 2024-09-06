import sys
sys.stdin = open("sample_input.txt")

# def binary_search(l, target):
#     low = 1
#     high=l
#     cnt = 0
#     while low <= high:
#         cnt+=1
#         mid = (low + high) // 2
#         if mid == target:
#             return cnt
#         elif mid < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return cnt

cnt=0
def binary_search(low, high, x):
    global cnt
    if high >= low:
        cnt += 1
        mid = (high + low) // 2
        if mid == x:
            return cnt
        elif mid > x:
            return binary_search(low, mid, x)
        else:
            return binary_search(mid, high, x)
    else:
        return cnt

for t in range(1, int(input())+1):
    l, afind, bfind = map(int, input().split())
    cnt=0
    a=binary_search(1, l, afind)
    cnt=0
    b=binary_search(1, l, bfind)
    if a<b:
        print(f'#{t} A')
    elif a>b:
        print(f'#{t} B')
    else:
        print(f'#{t} 0')