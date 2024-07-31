import sys
sys.stdin = open('input.txt', 'r')


for t in range(1, int(input())+1):
    N , K = map(int, sys.stdin.readline().split())
    
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    re = 0
    for i in range(N):
        for j in range(N-K+1):
            uj = 0
            for k in range(K):
                uj+=arr[i][j+k]
            if uj == k:
                try:
                    if arr[i][j-1]==0 and arr[i][j+k+1]==0:
                        re+=1
                except IndexError:
                    if 0<=(j-1):# and (j+k+1)==N:
                        if arr[i][j-1]==0:
                            re+=1
                    elif (j+k+1)<N:# and 0>(j-1):
                        if arr[i][j+k+1]==0:
                            re+=1
    for i in range(N-K+1):
        for j in range(N):
            uj = 0
            for k in range(K):
                uj+=arr[i+k][j]
            if uj == k:
                try:
                    if arr[i-1][j]==0 and arr[i+k+1][j]==0:
                        re+=1
                except IndexError:
                    if 0<=(i-1):# and (i+k+1)==N:
                        if arr[i-1][j]==0:
                            re+=1
                    elif (i+k+1)<N:# and 0>(i-1):
                        if arr[i+k+1][j]==0:
                            re+=1
    
    print(f'#{t} {re}')
            
                