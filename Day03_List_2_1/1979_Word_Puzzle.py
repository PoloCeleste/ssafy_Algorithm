for t in range(1, int(input())+1):
    N , K = map(int, input().split())
    
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    for i in range(N):
        for j in range(N-K+1):
            uj = 0
            for k in range(K):
                uj+=arr[i][j+k]
            if uj == k:
                try:
                    t=0
                    if arr[i][j-1] == 0:
                        pass
                except:
                    pass
            
                