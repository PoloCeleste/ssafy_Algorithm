for t in range(int(input())):
    N, M=map(int, input().split())
    A, B=list(map(int,input().split())), list(map(int,input().split()))
    if N==M: c=sum(A[i]*B[i] for i in range(N))
    elif N>M: c=max(sum(A[j+i]*B[j] for j in range(M)) for i in range(N-M+1))
    else: c=max(sum(A[j]*B[j+i] for j in range(N)) for i in range(M-N+1))
    print(f'#{t+1} {c}')
