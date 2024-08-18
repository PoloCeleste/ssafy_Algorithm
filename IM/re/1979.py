import sys
sys.stdin = open('input.txt','r')

for t in range(1,int(input())+1):
    N,K=map(int, input().split())
    arr=[[0]*(N+2)]
    arr.extend([[0]+list(map(int, input().split()))+[0] for _ in range(N)])
    arr.extend([[0]*(N+2)])
    c=0
    for i in range(1,N+1):
        for j in range(1,N-K+2):
            if sum(arr[i][j:j+K])==K and arr[i][j-1]==0 and arr[i][j+K]==0: c+=1
            if sum(arr[j+k][i] for k in range(K))==K and arr[j-1][i]==0 and arr[j+K][i]==0: c+=1
    print(f'#{t} {c}')