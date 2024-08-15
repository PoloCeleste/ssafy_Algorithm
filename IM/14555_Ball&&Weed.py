for t in range(int(input())):
    print(f"#{t+1} {list(input().replace('()','0').replace('(|','0').replace('|)','0')).count('0')}")
