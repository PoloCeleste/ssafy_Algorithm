import sys
z_n = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
str_to_n = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}
sys.stdin = open("GNS_test_input.txt")

    
def GNS1():
    N=int(input().split()[1]) # 숫자단어 개수 받기
    arr = input().split() # 정렬 전 문자열 받기 
    cnt=[0]*10 # 단어 개수 저장
    for i in range(10): # 기준문자열 길이만큼 순회하며
        for a in arr: # 단어 개수 만큼 순회
            if a==z_n[i]: # 단어 배열 순회하며 현재 기준과 같은 숫자단어 찾으면
                cnt[i]+=1 # 단어 개수 +1
    
    print(f"#{t}")
    for i in range(10): # 기준배열 순회하며
        print((z_n[i]+' ')*cnt[i], end='') # 개수만큼 출력
    print()


def GNS2():
    N=int(input().split()[1]) # 숫자단어 개수 받기
    arr = input().split() # 정렬 전 문자열 받기
    result=''
    for n in z_n:
        for word in arr:
            if word == n:
                result+=(word+' ')
    
    print(f"#{t} {result}")
    
    
def GNS3():
    tc, n = input().split()
    words = input().split()
    max_value = 9
    cnt=[0]*(max_value+1)
    for word in words:
        cnt[str_to_n[word]]+=1
    
    result=[]
    for i,c in enumerate(cnt):
        result.append([z_n[i]]*c)
    
    print(f"#{t} {result}")
    

for t in range(1, int(input())+1): # 테스트케이스만큼 반복
    GNS1()
    #GNS2()
    #GNS3()