for t in range(1,int(input())+1):
    N, M = map(int, input().split())
    print(f'#{t} {list(map(int, input().split()))[M%N]}')