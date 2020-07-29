from datetime import date

def solution(a, b):
    return date(2016, a, b).strftime("%a").upper()

print(solution(5, 24))