def solution(n, arr1, arr2):
    answer = [format(i|j, str(n)+'b').replace('1','#').replace('0',' ') for i, j in zip(arr1, arr2)]
    return answer

print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))