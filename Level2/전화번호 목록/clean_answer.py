def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    #리스트 for을 하면 어차피 다은꺼 가져오니깐 zip으로 묶음
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True