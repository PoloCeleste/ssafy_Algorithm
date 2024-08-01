# import copy
# def bubble_sort(origin, dump):
#     cnt=[0]*dump
#     for i in range(dump-1, 0, -1):
#         arr=copy.deepcopy(origin)
#         for j in range(i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 cnt[i]+=1
#     return cnt  ##### 고정된 상태에서 비교해야 가능
#### 버블정렬은 계속 바뀌므로 불가

# T = int(input())
# for i in range(1, T+1):
#     dump = int(input())
#     arr=list(map(int, input().split()))
#     if dump==1:
#         print(f'#{i} 0')
#         continue
#     cnt=bubble_sort(arr, dump)
#     mx =0
#     for j in range(dump):
#         print(dump-(j+1)-cnt[j])
#         if mx<=cnt[j]:mx=cnt[j]
#     print(f'#{i} {mx}')
    
    
# for t in range(1, int(input())+1): #테스트케이스
#     N = int(input()) # 가로 길이
#     boxes = list(map(int, input().split())) # 건물 배열

#     max_distance = 0 # 최대 낙차
 
#     for i in range(N): #길이만큼 반복
#         cnt = 0 # 낙차 카운트
#         for j in range(i+1, N): 
#             if boxes[i] <= boxes[j]: cnt += 1 
#         print(N - 1 - i - cnt)
#         max_distance = max(max_distance, N - 1 - i - cnt) # 현재 최대값과  비교해서 최대값 저장
#         print(max_distance)
 
#     print(f'#{t}', max_distance)