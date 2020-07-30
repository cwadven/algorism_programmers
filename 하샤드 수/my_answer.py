def solution(x):
    if x/sum([int(i) for i in str(x)]) % 1 == 0:
        return True
    else:
        return False

print(solution(12))