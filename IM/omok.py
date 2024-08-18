dij=[[0,1],[1,1],[1,0],[1,-1]]
def f():
    N=int(input())
    arr=[input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for di,dj in dij:
                c=0
                for k in range(5):
                    ni,nj=i+di*k,j+dj*k
                    if ni<0 or nj<0 or ni>=N or nj>=N:continue
                    if arr[ni][nj]=='.':break
                    c+=1
                if c==5:return 'YES'
    return 'NO'
for t in range(int(input())): print(f'#{t+1} {f()}')