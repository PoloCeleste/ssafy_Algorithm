v=[]
def solution(begin, target, words):
    if target not in words: return 0
    N=len(words)
    n=len(target)
    result=[]
    global v
    v=[0]*N
    def f(b, crr):
        if b==target:
            result.append(len(crr))
            return
        x=[0]*N
        for w in range(N):
            if v[w]:
                x[w]=1
                continue
            c=0
            for i in range(n):
                if words[w][i]==b[i]:c+=1
            if c!=(n-1):x[w]=2
        for w in range(N):
            if x[w] or v[w]:continue
            v[w]=1
            f(words[w], crr+[words[w]])
            v[w]=0
    f(begin,[])
    return min(result)

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))