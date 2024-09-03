import sys
sys.stdin=open('5201_input.txt', 'r')

def bubble(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j]<arr[j+1]:arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

for t in range(1, int(input())+1):
    N,M=map(int,input().split())
    wL=bubble(list(map(int, input().split())))
    tL=bubble(list(map(int, input().split())))
    cnt=0
    st=0
    for tr in tL:
        if st==N:break
        for w in range(st,N):
            if wL[w]>tr:
                st+=1
                continue
            cnt+=wL[w]
            st+=1
            break

    print(f'#{t} {cnt}')