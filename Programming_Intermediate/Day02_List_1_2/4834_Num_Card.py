for t in range(1, int(input())+1):
    N=int(input())
    arr = [0]*10
    for i in input(): arr[int(i)] += 1
    mx, mx_c=0,0
    for x in range(10):
        if mx<=arr[x]:
            mx=arr[x]
            mx_c=x
    print(f'#{t} {mx_c} {mx}')