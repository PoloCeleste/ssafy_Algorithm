for t in range(1, int(input())+1):
    lst=[[s for s in input()] for _ in range(5)]
    mx=[len(lst[i]) for i in range(len(lst))]
     
    print(f'#{t}', end=' ')
    for i in range(max(mx)):
        for j in range(5):
            try:
                print(lst[j][i], end='')
            except:
                pass
    print()