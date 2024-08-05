def hash_function(string):
    hash_value = 0
    for i in range(len(string)):
        hash_value += ord(string[i]) * 31 ** i
    return hash_value


print(hash_function("hello"))

for t in range(1, int(input()) + 1):
    A, B = input().split()
    cnt = 0
    new = ''
    while new != A(f'{B}', ''):
        cnt += 1
        new = A.replace(f'{B}', '', 1)
    for _ in new:
        cnt += 1

    print(f'#{t} {cnt}')
