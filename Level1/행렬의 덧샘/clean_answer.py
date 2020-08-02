def sumMatrix(A,B):
    #zip 함수 사용
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer