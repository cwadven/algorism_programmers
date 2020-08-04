def solution(prices):
    answer = [0] * len(prices)
    for index, i in enumerate(prices):
        for j in range(index+1, len(prices)):
            answer[index] = answer[index] + 1
            if i > prices[j]:
                break
    return answer

print(solution([1, 2, 3, 2, 3, 3, 1]))