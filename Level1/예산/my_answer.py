def solution(d, budget):
    count = 0

    while(budget>0):
        if len(d):
            _min = min(d)
        else:
            break
        budget = budget - _min
        if budget < 0:
            break
        count = count + 1
        d.remove(_min)

    return count

print(solution([1,2], 10))