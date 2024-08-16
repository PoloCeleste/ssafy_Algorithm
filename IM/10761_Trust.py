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
    btn['b'], btn['o'] = btnb, btno
    def Robot(C_road, C, check, cnt, info=True):
        global btn
        if C_road[C]==cnt:
            if not info: return C, True, cnt, C_road
            cnt+=1
            C_road[C]=-1
            if check=='b':
                if cnt==O_road[O]:return C, False, cnt, C_road #
                else: return C, True, cnt, C_road
            else: return C, True, cnt, C_road
        else:
            # 현 위치가 눌러야할 버튼이 아닐 경우 만약 해당 길의 다음버튼 위치이면 멈춰서 기다리고
            # 아무것도 없다면 다음 위치를 향해 이동
            # 다음 위치가 없다면 계속 위로 이동
            for d in [s for s in range(cnt, N)]:
                if C_road[C]==d:
                    return C, True, cnt, C_road
                elif d in C_road:
                    if C_road.index(d)>C: return C+1, True, cnt, C_road
                    else: return C-1, True, cnt, C_road
            else: return C+1, True, cnt, C_road

    while cnt!=N:
        time+=1
        B, Orange, cnt, B_road=Robot(B_road, B, 'b', cnt)
        O, _, cnt, O_road=Robot(O_road, O, 'o', cnt, Orange)

    print(f'#{t} {time}')