def KMP(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = [0]*m
    j = 0
    computeLPS(pattern, m, lps)
    i = 0
    cnt = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            cnt += 1
            j = lps[j-1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return cnt

def computeLPS(pattern, m, lps):
    l = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[l]:
            l += 1
            lps[i] = l
            i += 1
        else:
            if l != 0:
                l = lps[l-1]
            else:
                lps[i] = 0
                i += 1

def BruteForce(target, pattern):
    M=len(pattern)
    N=len(target)
    i = 0  # t의 인덱스
    j = 0  # p의 인덱스
    cnt=0
    while j < M and i < N :
        if target[i] != pattern[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == M: cnt+=1  # 검색 성공
    else: cnt+=1  # 검색 실패
    return cnt

for t in range(1, int(input()) + 1):
    A, B = input().split()
    print(BruteForce(A, B))
    result = 0
    pattern_idx = 0
    compare_idx = 0

    while compare_idx < len(B):
        if B[compare_idx] != A[pattern_idx]:
            compare_idx = compare_idx - pattern_idx + 1
            pattern_idx = 0
            continue
        pattern_idx += 1
        compare_idx += 1

        if pattern_idx == len(A):
            result += 1
            pattern_idx = 0
            compare_idx = compare_idx - pattern_idx + 1
    print(f'#{t} {count}')
