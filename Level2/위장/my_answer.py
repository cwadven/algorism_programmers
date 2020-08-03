def solution(clothes):
    operation = []
    answer = 1
    _get = list([i[1] for i in clothes])
    unique_get = list(set(_get))

    for i in unique_get:
        operation.append(_get.count(i))

    for i in operation:
        answer = answer * (i + 1)

    answer = answer - 1

    return answer

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])