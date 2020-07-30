def solution(arr):
    #결과 값이 정수로 나오도록 하기 위해서 if 문사용
    return sum(arr)/len(arr) if str(sum(arr)/len(arr))[-1] != "0" else int(sum(arr)/len(arr))

print(solution([5,5]))