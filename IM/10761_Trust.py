import sys
sys.stdin = open('10761_input.txt', 'r')

for t in range(1, int(input())+1):
    arr = input().split()
    N, arr = int(arr[0]), arr[1:]
    cnt=0
    Blue, Orange = True, True
    B_road = [-1]*101
    B, O= 1, 1
    O_road = [-1]*101
    btn = {}
    time=0
    btnb, btno=[],[]
    for i in range(0, N*2, 2):
        if arr[i]=='B':
            B_road[int(arr[i+1])]=(i//2)
            btnb.append(int(arr[i+1]))
        elif arr[i]=='O':
            O_road[int(arr[i+1])]=(i//2)
            btno.append(int(arr[i+1]))
    bdic, odic={}, {}
    for b in btnb:
        BO=[o for o in btno if b>=o]
        bdic[b]=BO
    for o in btno:
        OB=[b for b in btnb if o>=b]
        odic[o]=OB
    btn['b'], btn['o'] = bdic, odic
    def Robot(C_road, C, check, val, cnt, info=True):
        global btn
        if C_road[C]==cnt:
            x=[w for w in btn[check][C]]
            if x:
                if C not in x:return C, True, cnt, C_road
            if not info: return C, True, cnt, C_road
            for value in btn[val].values():
                if C in value:value.remove(C)
            cnt+=1
            C_road[C]=-1
            if check=='b':
                if cnt==O_road[O]:return C, False, cnt, C_road
                else: return C, True, cnt, C_road
            else:
                if cnt==B_road[B]:return C, False, cnt, C_road
                else: return C, True, cnt, C_road
        else:
            for d in [s for s in range(cnt, N)]:
                if C_road[C]==d:
                    return C, True, cnt, C_road
                elif d in C_road:
                    if C_road.index(d)>C:
                        return C+1, True, cnt, C_road
                    else: return C-1, True, cnt, C_road
            else: return C+1, True, cnt, C_road

    while cnt!=N:
        time+=1
        B, Orange, cnt, B_road=Robot(B_road, B, 'b','o', cnt)
        O, _, cnt, O_road=Robot(O_road, O, 'o','b', cnt, Orange)

    print(f'#{t} {time}')