import sys
sys.stdin=open('5202_input.txt', 'r')

def bubble(arr,N):
    for i in range(N):
        for j in range(N-1):
            if arr[j][1]>arr[j+1][1]:arr[j], arr[j+1]=arr[j+1], arr[j]
    return arr

for t in range(1, int(input())+1):
    N=int(input())
    arr=bubble([tuple(map(int, input().split())) for _ in range(N)],N)
    end=arr[0][1]
    cnt=1
    for a in range(1,N):
        if arr[a][0]>=end:
            end=arr[a][1]
            cnt+=1

    print(f'#{t} {cnt}')