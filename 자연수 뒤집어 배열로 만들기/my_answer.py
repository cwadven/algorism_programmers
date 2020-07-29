def solution(n):
    p=list()
    
    for i in range(len(str(n))):
        p.append(int(str(n)[-1:]))
        n = str(n)[:len(str(n))-1]
    
    return p

print(solution(123456))