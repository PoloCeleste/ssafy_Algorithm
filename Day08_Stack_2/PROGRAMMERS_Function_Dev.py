def solution(progresses, speeds):
    answer, cnt = [], 0
    while speeds != []:
        for i in range(len(speeds)):
            if progresses[i] >= 100: continue
            progresses[i] += speeds[i]
        while speeds != [] and progresses[0] >= 100:
            cnt += 1
            progresses.pop(0)
            if progresses != [] and progresses[0] < 100:
                answer.append(cnt)
                cnt = 0
            elif len(progresses) == 0 and cnt != 0: answer.append(cnt)
            speeds.pop(0)
    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))