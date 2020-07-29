def nextSqure(n):
    sqrt = n ** (1/2)

    #정수일 경우 1 나머지를면 나누어 떨어지지만 소수일 경우 나머지가 있다!!
    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return 'no'