def solution(dartResult):
    first_check = 0
    check = 0
    pre = []
    for count, i in enumerate(dartResult):
        if not i.isdigit():
            if dartResult[first_check:count]:
                pre.append(int(dartResult[first_check:count])) # print(dartResult[first_check:count]) #숫자

            first_check = count+1

            if dartResult[count] == 'S':
                pre[check] = pre[check] ** 1
                check = check + 1
            elif dartResult[count] == 'D':
                pre[check] = pre[check] ** 2
                check = check + 1
            elif dartResult[count] == 'T':
                pre[check] = pre[check] ** 3
                check = check + 1

            elif dartResult[count] == '*':
                pre[check-1] = pre[check-1] * 2
                if check-1 == 0:
                    pass
                else:
                    pre[check-2] = pre[check-2] * 2
            elif dartResult[count] == '#':
                pre[check-1] = pre[check-1] * -1

    return sum(pre)

print(solution("1D2S3T*"))