def solution(n):
    start_list = [True] * (n+1)

    #n의 최대 약수는 n의 루트까지이다!
    #즉 이 의미는 10의 약수는 1,2,5,10이지만 이 약수는 결국 5 같이 그 이상은 없음
    m = int((n-1) ** 0.5)

    for i in range(2, m+1):
        if start_list[i] == True:
            for j in range(i+i, n+1, i): #i이우 i의 배수들을 False로 변경
                start_list[j] = False

    print(start_list)
    return len([i for i in range(2,n+1) if start_list[i] == True])

print(solution(10))