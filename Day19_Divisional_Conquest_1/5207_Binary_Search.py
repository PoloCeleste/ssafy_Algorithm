import sys
sys.stdin=open('5207_input.txt', 'r')

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    Narr=sorted(list(map(int, input().split())))
    Marr=list(map(int, input().split()))
    cnt=0

    def binary_search(target):
        l = 0
        r = len(Narr) - 1
        R=True
        L=True
        while l <= r:
            mid = (l + r) // 2
            if Narr[mid] == target: return True
            elif Narr[mid] > target:
                if R:
                    r = mid - 1
                    R=False
                    L=True
                else: return False
            else:
                if L:
                    l = mid + 1
                    L=False
                    R=True
                else: return False
        return False

    for M in Marr:
        if binary_search(M):cnt+=1

    print(f'#{t} {cnt}')