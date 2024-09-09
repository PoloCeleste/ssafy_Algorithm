re=[0]
for t in range(int(input())):
    N,M=map(int, input().split())
    M=bin(M)[2:]
    re.append('1'*N==M[-N:])
for i, r in enumerate(re):
    if not i:continue
    if r:print(f'#{i} ON')
    else:print(f'#{i} OFF')