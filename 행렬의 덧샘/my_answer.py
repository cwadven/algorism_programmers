def solution(arr1, arr2):
    result = arr2
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            result[i][j] = arr1[i][j] + arr2[i][j]
    return result

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))