ls= [2, 3, 5, 7, 11]
for i in range(1, int(input())+1):
    n = int(input())
    result=[0]*5
    for j in range(5):
        while n%ls[j]==0:
            result[j]+=1
            n //=ls[j]
    print(f'#{i} {" ".join(list(map(str, result)))}')