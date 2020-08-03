def solution(progresses, speeds):
    count_list = []
    _pop = []
    while progresses:
        count = 0
        # while 문 한번에 speed 만큼 더한다,
        for i in range(len(progresses)):
            progresses[i] = progresses[i] + speeds[i]
            # 100 이상일 경우 100으로 퉁친다
            if progresses[i] > 100:
                progresses[i] = 100

        for j in range(len(progresses)):
            # (조건) 맨 앞에 있는게 100 이 될때
            if progresses[j] == 100:
                _pop.append(j)
                count = count + 1
            else:
                break

        _pop.sort(reverse=True)

        for k in _pop:
            progresses.pop(k)
            speeds.pop(k)

        if count:
            count_list.append(count)
        
        _pop = []

    return count_list

print(solution([93,93,93], [1,1,1]))