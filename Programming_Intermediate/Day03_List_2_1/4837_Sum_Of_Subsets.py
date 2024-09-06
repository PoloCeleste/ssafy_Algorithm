arr = [1,2,3,4,5,6,7,8,9,10,11,12] # 주어진 집합 A
n = len(arr) # 원소의 개수

for t in range(1, int(input())+1): # 테스트 케이스만큼 루프
    re=0 # 해당하는 부분집합 개수
    N, K = map(int, input().split()) # N개의 원소를 가지며 합이 K인 부분집합 찾기
    for i in range(1<<n): # 1<<n : 부분 집합의 개수 (2진수)
        a = [] # 빈 부분집합 생성
        for j in range(n): # 원소의 수만큼 비트를 비교함
            if i & (1<<j): # i의 j번 비트가 1인 경우
                a.append(arr[j]) # j번 원소 추가
        if len(a)==N and sum(a)==K: # 완성된 부분집합이 조건을 만족하면
            re+=1 # 개수 +1
    
    print(f'#{t} {re}') # 최종 결과 출력

# 주말 복습 코드
# A = [1,2,3,4,5,6,7,8,9,10,11,12]
# length = 0
# for _ in A: length += 1
#
# for t in range(1, int(input())+1):
#     N, K = map(int, input().split())
#     result = 0
#     for i in range(1 << length):
#         subs = []
#         for j in range(length):
#             if i & (1 << j):
#                 subs.append(A[j])
#         cnt, s = 0, 0
#         for sub in subs:
#             cnt += 1
#             s += sub
#         if cnt == N and s == K:
#             result += 1
#
#     print(f'#{t} {result}')