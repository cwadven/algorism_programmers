def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
    # 약수는 본 수의 반절 이상인 약수는 존재하지 않는다
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])