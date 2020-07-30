def solution(n, m):
    answer = [1]
    # 최대공약수
    for i in range(1, n+1):
        if n % i == 0 and m % i == 0:
            answer[0] = i

    # 최소공배수
    if m % i == 0:
        answer.append(m)
    else:
        answer.append(int(n*m/answer[0]))
    return answer

print(solution(2, 5))