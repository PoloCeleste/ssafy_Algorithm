import sys
z_n = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
# 기준 문자열


sys.stdin = open("GNS_test_input.txt")
for t in range(1, int(input())+1): # 테스트케이스만큼 반복
    N=int(input().split()[1]) # 숫자단어 개수 받기
    arr = input().split() # 정렬 전 문자열 받기
    cnt=[0]*10 # 단어 개수 저장
    for i in range(10): # 기준문자열 길이만큼 순회하며
        for j in range(N): # 단어 개수 만큼 순회
            if arr[j]==z_n[i]: # 단어 배열 순회하며 현재 기준과 같은 숫자단어 찾으면
                cnt[i]+=1 # 단어 개수 +1
    
    print(f"#{t}")
    for i in range(10): # 기준배열 순회하며
        print((z_n[i]+' ')*cnt[i], end='') # 개수만큼 출력
    print()