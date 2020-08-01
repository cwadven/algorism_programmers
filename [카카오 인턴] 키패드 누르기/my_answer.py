def solution(numbers, hand):
    #누른 것 위치 저장 필요
    left_save_current = 10
    right_save_current = 12
    answer = ''
    a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12],
    ]
    # 1 --> [0][0] 숫자 % 4 - 1
    # 2 --> [0][1]
    # 3 --> [0][2]

    # 4 --> [1][0]
    # 5 --> [1][1]
    # 6 --> [1][2]

    # 7 --> [2][0]
    # 8 --> [2][1]
    # 9 --> [2][2]

    # * --> [3][0] 10
    # 0 --> [3][1] 11
    # # --> [3][2] 12

    for i in numbers:
        left_count = 0
        right_count = 0
        if i in (1, 4, 7, '*'):
            answer = answer + 'L'
            left_save_current = i
            # print(a[left_save_current//3][left_save_current-1%3])
        elif i in (3, 6, 9, '#'):
            answer = answer + 'R'
            right_save_current = i
            # print(a[right_save_current//3][right_save_current-1%3])
        else:
            if i == 0:
                i = 11
            #왼손 거리 찾기
            #배열 위치의 값

            if i == a[(right_save_current-1)//3][(right_save_current-1)%3]:
                answer = answer + 'R'
                right_save_current = i
                continue
            elif i == a[(left_save_current-1)//3][(left_save_current-1)%3]:
                answer = answer + 'L'
                right_save_current = i
                continue

            all_count = 0

            for j in range((i-1)//3,len(a)): # 밑으로
                if a[j][(i-1)%3] == a[(right_save_current-1)//3][(right_save_current-1)%3]:
                    right_count = all_count
                    break
                all_count = all_count + 1

            all_count = 0

            for j in range((i-1)//3,-1,-1): # 위로
                if a[j][(i-1)%3] == a[(right_save_current-1)//3][(right_save_current-1)%3]:
                    right_count = all_count
                    break
                all_count = all_count + 1

            all_count = 0

            for k in range((i-1)%3,len(a[0])): # 오른쪽
                if a[(i-1)//3][k] == a[(right_save_current-1)//3][(right_save_current-1)%3]:
                    right_count = all_count
                    break
                all_count = all_count + 1

            all_count = 0

            for k in range((i-1)%3,-1,-1): # 왼쪽
                if a[(i-1)//3][k] == a[(right_save_current-1)//3][(right_save_current-1)%3]:
                    right_count = all_count
                    break
                all_count = all_count + 1
                
            ##################################

            all_count = 0

            for j in range((i-1)//3,len(a)): # 밑으로
                if a[j][(i-1)%3] == a[(left_save_current-1)//3][(left_save_current-1)%3]:
                    left_count = all_count
                    break
                all_count = all_count + 1

            all_count = 0

            for j in range((i-1)//3,-1,-1): # 위로
                if a[j][(i-1)%3] == a[(left_save_current-1)//3][(left_save_current-1)%3]:
                    left_count = all_count
                    break
                all_count = all_count + 1

            all_count = 0

            for k in range((i-1)%3,len(a[0])): # 오른쪽
                if a[(i-1)//3][k] == a[(left_save_current-1)//3][(left_save_current-1)%3]:
                    left_count = all_count
                    break
                all_count = all_count + 1

            all_count = 0

            for k in range((i-1)%3,-1,-1): # 왼쪽
                if a[(i-1)//3][k] == a[(left_save_current-1)//3][(left_save_current-1)%3]:
                    left_count = all_count
                    break
                all_count = all_count + 1
                
            # print(i,left_count, right_count)

            if right_count > 0 and left_count > 0:
                if right_count < left_count:
                    answer = answer + 'R'
                    right_save_current = i
                elif right_count > left_count:
                    answer = answer + 'L'
                    left_save_current = i
                else: #같을 경우
                    if hand == "right":
                        answer = answer + 'R'
                        right_save_current = i
                    elif hand == "left":
                        answer = answer + 'L'
                        left_save_current = i
            elif right_count > 0 and left_count == 0:
                answer = answer + 'R'
                right_save_current = i
            elif right_count == 0 and left_count > 0:
                answer = answer + 'L'
                left_save_current = i
            else:
                if right_count == 0 and left_count == 0:
                    count2 = 0
                    for m in range((i-1)//3,-1,-1): #위쪽
                        if a[m][(i-1)%3-1] == a[(left_save_current-1)//3][(left_save_current-1)%3] or a[m][(i-1)%3+1] == a[(left_save_current-1)//3][(left_save_current-1)%3]:
                            count2 = count2 + 1
                            left_count2 = count2
                        if a[m][(i-1)%3-1] == a[(right_save_current-1)//3][(right_save_current-1)%3] or a[m][(i-1)%3+1] == a[(right_save_current-1)//3][(right_save_current-1)%3]:
                            count2 = count2 + 1
                            right_count2 = count2
                        count2 = count2 + 1

                    count2 = 0
                    for m in range((i-1)//3,len(a)): #아래쪽
                        if a[m][(i-1)%3-1] == a[(left_save_current-1)//3][(left_save_current-1)%3] or a[m][(i-1)%3+1] == a[(left_save_current-1)//3][(left_save_current-1)%3]:
                            count2 = count2 + 1
                            left_count2 = count2
                        if a[m][(i-1)%3-1] == a[(right_save_current-1)//3][(right_save_current-1)%3] or a[m][(i-1)%3+1] == a[(right_save_current-1)//3][(right_save_current-1)%3]:
                            count2 = count2 + 1
                            right_count2 = count2
                        count2 = count2 + 1

                    # print(i,left_count2, right_count2)

                    if left_count2 < right_count2:
                        answer = answer + 'L'
                        left_save_current = i
                    elif left_count2 > right_count2:
                        answer = answer + 'R'
                        right_save_current = i
                    else:
                        if hand == "right":
                            answer = answer + 'R'
                            right_save_current = i
                        elif hand == "left":
                            answer = answer + 'L'
                            left_save_current = i
                    
                else:
                    if hand == "right":
                        answer = answer + 'R'
                        right_save_current = i
                    elif hand == "left":
                        answer = answer + 'L'
                        left_save_current = i

    return answer
    
print(solution([7,0,2], "left"))