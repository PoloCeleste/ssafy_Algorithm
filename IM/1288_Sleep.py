for t in range(int(input())):
    N=input()
    if N=='1':
        print(10)
        continue
    l=set()
    x=1
    result=0
    while 1:
        for n in range(int(N), int(N)*x+1, int(N)):
            result += 1
            for y in str(n):
                l.add(int(y))
        if len(l)==10:break
        x+=1
    print(result)