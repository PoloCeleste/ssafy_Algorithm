import sys, math
sys.stdin=open('1242_input.txt','r')
math.ce
pass1=['0001101','0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011']
pass2=[''.join([p+p for p in p1]) for p1 in pass1]

for t in range(1, int(input())+1):
    N,M=map(int,input().split())
    arr=list(set(sys.stdin.readline() for _ in range(N)))[1:]

    pa=''
    passList=set()
    for ar in arr:# 개행 지우기
        ar=ar.strip()
        for a in range(M):
            if ar[a]=='0':
                if pa:
                    if pa in passList:
                        p=''
                        continue
                    if a+1<M and a-1>=0 and (ar[a-1]!='0' or ar[a+1]!='0'):
                        pa += ar[a]
                        continue
                    if a+1<M and a-1>=0 and (ar[a-1]!='0' or ar[a+1]!='0'):
                        pa += ar[a]
                        continue
                    else:
                        if pa.endswith('0'):
                            pa = pa.strip('0')
                        passList.add(pa)
                        pa=''
                else: continue
            else: pa+=ar[a]
        if pa:
            if pa.endswith('0'):
                pa=pa.strip('0')
            passList.add(pa)
    print(passList)
    print(N,M)