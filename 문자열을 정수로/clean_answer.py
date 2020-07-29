# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
def strToInt(str):
    result = 0

    #뒤에서 부터 증가 시키기
    for idx, number in enumerate(str[::-1]):
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)

    return result


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(strToInt("-1234"))