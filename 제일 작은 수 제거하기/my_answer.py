def solution(arr):
    arr.remove(min(arr))
    if len(arr):
        return arr
    else:
        return [-1]
    

print(solution([10]))