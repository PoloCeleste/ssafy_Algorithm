for i in range(1, 11):
    n=int(input())
    sm=0
    arr = list(map(int, input().split()))
    for x in range(2, n-1):
        if (arr[x] > arr[x-1] and arr[x] > arr[x-2]) and (arr[x] > arr[x+1] and arr[x] > arr[x+2]):
            a=[]
            a.append(arr[x]-arr[x-1])
            a.append(arr[x]-arr[x-2])
            a.append(arr[x]-arr[x+1])
            a.append(arr[x]-arr[x+2])
            m=a[0]
            for y in a:
                if y<m:m=y
            sm+=m
    print(f'#{i} {sm}')
    
    
    
