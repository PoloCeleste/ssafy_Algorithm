def reverse(s):
    if len(s)==0: return s
    else: return reverse(s[1:])+s[0]
 
for t in range(1, int(input())+1):
    s=input().strip()
    re_s=reverse(s).replace('b', 'D').replace('d', 'B').replace('q', 'P').replace('p', 'Q').lower()
    print(f'#{t} {re_s}')