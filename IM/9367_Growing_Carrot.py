import sys
sys.stdin = open('carrot_sample_in.txt', 'r')

for t in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = []
    a = [arr[0]]
    for i in range(1, N):
        if arr[i] <= arr[i-1]:
            cnt.append(len(a))
            a=[]
        a.append(arr[i])
    cnt.append(len(a))

    if max(cnt) == 0:
        print(f'#{t} 1')
    else: print(f'#{t} {max(cnt)}')