def solution(n):
    answer = ''

    # 와 알고리즘 너무 어렵다...
    # 3개 이기 때문에 %3하고 0일 경우는 없으니깐 0일때는 4로만 들고 몫을 -1을 한다
    while n > 0:
        a = n%3

        if a == 0:
            a = 4
            n = (n//3)-1
        else:
            n = (n//3)
        
        answer = str(a) + answer
    
    return answer

print(solution(13))