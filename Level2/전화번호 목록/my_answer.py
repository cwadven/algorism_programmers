def solution(phone_book):
    answer = list(map(str, sorted(map(int, phone_book))))

    for index, i in enumerate(answer):
        for j in range(index+1, len(answer)):
            if i == answer[j][:len(i)]:
                return False

    return True

print(solution(['12', '123', '1235', "567", "88"]))