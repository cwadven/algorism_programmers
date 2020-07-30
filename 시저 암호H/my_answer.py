def solution(s, n):
    #나머지 이용
    a = []
    for i in s:
        if ord(i)>=65 and ord(i)<=90:
            b = ((ord(i)+n-65)%26)+65 # 0이랑 25랑 지금 똑같아서 n을 하면
            a.append(chr(b))
        elif ord(i)>=97 and ord(i)<=122:
            b = ((ord(i)+n-97)%26)+97
            a.append(chr(b))
        elif i == " ":
            a.append(i)

    return ''.join(a)

print(solution('a B z', 4))
