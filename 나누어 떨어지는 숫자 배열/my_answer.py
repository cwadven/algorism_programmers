def solution(arr, divisor):
    result = list()
    for i in arr:
        if i % divisor == 0:
            result.append(i)
    if not result:
        result.append(-1)
    else:
        result.sort()

    return result

print(solution([3,2,6], 10))