for i in range(1, int(input())+1):
    N=int(input())
    arr = []
    for j in range(N):
        s = list(map(int, input().split()))
        arr.append(s)
    P = int(input())
    c=[0]*P
    for j in range(P):
        c[j]=int(input())
    result={}
    result_l=[]
    for x in range(N):
        for y in range(arr[x][0], arr[x][1]+1):
            if y in result:
                result[y]+=1
            else : result[y]=1
    for a in c:
        if a in result:
            result_l.append(result[a])
        else:
            result_l.append(0)

    print(f"#{i}", end=' ')
    print(*result_l)