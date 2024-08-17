import sys
sys.stdin = open('10761_input.txt', 'r')
# 시간복잡도 n³
for t in range(1, int(input())+1):
    arr = input().split()
    N, arr = int(arr[0]), arr[1:]
    cnt, time=0, 0 # 버튼 누른 횟수와 시간
    Orange = True
    B_road, O_road={}, {} # 각 로봇에 할당된 버튼
    B, O= 1, 1 # 각 로봇의 초기 위치
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

# 반복문 사용 줄이기
# 시간복잡도 n²
for t in range(int(input())):  # 테케만큼 반복
    arr=input().split()  # 버튼 수열
    N=int(arr[0])*2  # 버튼 개수
    time=[0, 0]  # 각 로봇의 이동 시간
    robot={'B':1, 'O':1} # 각 로봇

    for i in range(1, N, 2):  # 버튼 개수만큼 반복
        btn=int(arr[i+1])
        if arr[i]=='B':
            time[0]+=abs(btn-robot['B'])+1  # 버튼과 로봇 사이 거리 == 이동 시간   # 버튼 누르는 거까지 시간 +1
            if time[0]<=time[1]:time[0]=time[1]+1
            # 만약 다른 로봇이 이전 버튼을 누른 시간이 현재 위치의 버튼을 누른 시간과 같거나 느리다면 그 시간에 +1하여 저장
            robot['B'] = btn  # 현재 위치를 버튼 위치로 변경
        else:
            time[1]+=abs(btn-robot['O'])+1
            if time[1]<=time[0]: time[1]=time[0]+1
            robot['O'] = btn

    print(f'#{t+1} {time}')

def f():
    a=input().split()
    B,O,Bl,Ol=0,0,1,1
    for i in range(1,int(a[0])*2,2):
        b=int(a[i+1])
        if a[i]=='B':
            B+=abs(b-Bl)+1
            if B<=O:B=O+1
            Bl=b
        else:
            O+=abs(b-Ol)+1
            if O<=B:O=B+1
            Ol=b
    return max(B,O)
for t in range(int(input())):print(f'#{t+1} {f()}')

def f():
    a=input().split()  # array ; 버튼 순열 받기
    r,c={'O':[1,0],'B':[1,0]},0  # Robot{이름:[위치,소요 시간]}, count ; 총 소요 시간 계산
    for i in range(1,int(a[0])*2,2):  # 버튼 순열 돌면서 버튼 위치와 그 버튼을 누를 로봇의 이름 가져오기
        n=a[i]  # name ; 로봇의 이름
        b=int(a[i+1])  # button ; 누를 버튼 위치
        d=abs(b-r[n][0])  # distance ; 버튼과 로봇 사이의 거리이자 로봇이 버튼까지 이동하는 시간
        T=c-r[n][1]  # time ; 총 소요 시간에서 이전의 로봇의 소요 시간 빼기 ; 동시 버튼누르기 검증 위함
        c+=(1 if d<=T else d-T+1)  # 만약 총 소요 시간에 이전 소요시간을 뺀 값이 현재 소요시간보다 크거나 같다면 총 소요시간에다 1을 더하고(이전 버튼을 누를 때까지 기다렸다 누르고)
        # 현재 소요시간보다 작다면 총 소요시간에 현재 로봇이 이동하고 버튼을 누르는 시간 추가
        r[n]=[b,c]  # 최종 위치와 소요시간을 해당 로봇에 저장
    return c  # 마지막 버튼을 누를 때까지 소요한 시간 반환
for t in range(int(input())):print(f'#{t+1} {f()}')