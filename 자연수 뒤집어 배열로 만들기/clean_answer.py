def digit_reverse(n):
    return list(map(int, reversed(str(n))))

def digit_reverse2(n):
    return [int(i) for i in str(n)][::-1]