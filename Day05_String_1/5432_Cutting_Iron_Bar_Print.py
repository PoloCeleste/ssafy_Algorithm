iron = input().replace('()', '0')
n=len(iron)

indices = [i for i, c in enumerate(iron) if c == '0']
arr = [[' ' for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if j in indices:
            if j+1 in indices: arr[i][j]='|-'
            else: arr[i][j]='|'
x=n-1
cut={}
for y in range(n):
    if iron[y]=='0':continue
    if iron[y]==')' and x+1<n: x+=1
    arr[x][y]='-'
    for i in range(1, n):
        if x+i<n:
            arr[x+i][y]='-'
    if iron[y]=='(' and x-1>=0: x-=1
    if y+1==n:continue
    if iron[y]+iron[y+1]==')(':
        arr[x][y]+=' '
        cut[y]=x

for a in range(n):
    for c in cut.keys():
        if arr[a][c]=='- ':continue
        else:
            if cut[c]<a:arr[a][c]+='-'
            else:arr[a][c]+=' '

for i in range(n):
    if '-' in arr[i]:
        print(''.join(arr[i]))