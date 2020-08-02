def solution(arr, divisor):
    #리스트 정규표현식
    return sorted([i for i in arr if i % divisor == 0]) or [-1]

print(solution([3,2,6], 10))