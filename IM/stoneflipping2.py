c=[1,0]
for t in range(1,int(input())+1):
    N, M = map(int, input().split())
    arr=list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())
        for x in range(1,j+1):
            if i-1+x>=N or i-1-x<0:break
            if arr[i-1+x]!=arr[i-1-x]:continue
            arr[i-1+x],arr[i-1-x]=c[arr[i-1+x]],c[arr[i-1+x]]
    print(f'#{t}', *arr)