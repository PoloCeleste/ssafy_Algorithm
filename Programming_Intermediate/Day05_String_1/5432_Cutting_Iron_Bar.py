for t in range(1, int(input())+1):
    iron=input().replace('()', '0')
    r, s=[], 0
    for i in iron:
        if i=='(' : r.append(1)
        elif i==')' : s+=r.pop()
        elif i=='0':
            for x in range(len(r)):
                r[x]+=1
    print(f'#{t} {s}')