def solution(d, budget):
    d.sort()

    #큰것을 하나하나씩 빼겠다는 기준으로 접근 했음!
    while budget < sum(d):
        d.pop()

    return len(d)

print(solution([1,3,2,5,4], 10))