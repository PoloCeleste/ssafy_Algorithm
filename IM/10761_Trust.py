import sys
sys.stdin = open('10761_input.txt', 'r')

for t in range(1, int(input())+1):
    arr = input().split()
    N, arr = int(arr[0]), arr[1:]
    cnt, time=0, 0
    Orange = True
    B_road, O_road={}, {}
    B, O= 1, 1
    for i in range(0, N*2, 2):
        if arr[i]=='B':
            B_road[int(arr[i+1])]=i//2
        elif arr[i]=='O':
            O_road[int(arr[i+1])]=i//2

    def Robot(c_road, C, check, cnt, info=True):
        if C in c_road and c_road[C]==cnt:
            if not info: return C, True, cnt, c_road
            cnt+=1
            del c_road[C]
            if check=='b':
                if O in O_road and cnt==O_road[O]:return C, False, cnt, c_road
                else: return C, True, cnt, c_road
            else: return C, True, cnt, c_road
        else:
            for loc, num in c_road.items():
                if num<cnt: continue
                if loc==C: return C, True, cnt, c_road
                elif loc>C: return C+1, True, cnt, c_road
                elif loc<C: return C-1, True, cnt, c_road
            else: return C + 1, True, cnt, c_road

    while cnt!=N and 0<B<=100 and 0<O<=100:
        time+=1
        B, Orange, cnt, B_road=Robot(B_road, B, 'b', cnt)
        O, _, cnt, O_road=Robot(O_road, O, 'o', cnt, Orange)

    print(f'#{t} {time}')

for t in range(int(input())):
    arr = input().split()
    N, arr = int(arr[0]), arr[1:]
    time=[0, 0]
    robot={'B':1, 'O':1} # 각 로봇 위치
    for i in range(0, N * 2, 2):
        if arr[i]=='B':
            d=arr[i+1]-robot['B']# 버튼과 로봇 사이 거리 == 이동시간
            time[0]+=d
            # 버튼 누르면 시간 +1
            # 다음 버튼 고려
            pass
        elif arr[i]=='O':

            pass

    print(f'#{t+1} {time}')