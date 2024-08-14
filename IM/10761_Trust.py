import sys
from collections import deque
sys.stdin = open('10761_input.txt', 'r')

for t in range(1, int(input())+1):
    arr = input().split()
    Blue, Orange = True, True
    N, arr = arr[0], arr[1:]
    cnt=0
    B_road = [0]*101
    B, O= 1, 1
    O_road = [0]*101
    btn = {'b':[], 'o':[]}
    time=0
    for i in range(0, int(N)*2, 2):
        if arr[i]=='B':
            B_road[int(arr[i+1])]=1
            btn['b'].append(int(arr[i+1]))
        elif arr[i]=='O':
            O_road[int(arr[i+1])]=1
            btn['o'].append(int(arr[i + 1]))
    btn['b'] = sorted(btn['b'])
    btn['o'] = sorted(btn['o'])
    print(btn)

    # while cnt!=N:
    #     time+=1
    #     if Blue:
    #         if B_road[B]==0:B+=1
    #         elif B_road[B]==1:
    #             if B_road[O] == 0:
    #                 B_road[B]=0
    #                 cnt+=1
    #     if Orange:
    #         if O_road[O]==0:O+=1
    #         elif O_road[O]==1:
    #             if B_road[O]==0:
    #                 cnt+=1

    print(N, arr)
