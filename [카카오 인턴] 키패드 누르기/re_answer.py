#이거 안된다고 합니다... 왜 안됐는지는 잘 모르겠습니다 ㅠㅠ
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

    for i in numbers:
        if i in (1, 4, 7, '*'):
            answer = answer + 'L'
            left_save_current = i
        elif i in (3, 6, 9, '#'):
            answer = answer + 'R'
            right_save_current = i
        else:
            if i == 0:
                i = 11
            if i == '*':
                i = 10
            if i == '#':
                i = 12
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
            
            left_count2 = 0
            right_count2 = 0

            count2 = 0
            for m in range((i-1)//3,-1,-1): #위쪽
                if a[m][(i-1)%3] == a[(left_save_current-1)//3][(left_save_current-1)%3]:
                    left_count2 = count2
                    

                elif a[m][(i-1)%3-1] == a[(left_save_current-1)//3][(left_save_current-1)%3]:
                    count2 = count2 + 1
                    left_count2 = count2
                    if left_count2:
                        count2 = count2 - 1
                    
                if a[m][(i-1)%3] == a[(right_save_current-1)//3][(right_save_current-1)%3]:
                    right_count2 = count2
                    
                    
                elif a[m][(i-1)%3+1] == a[(right_save_current-1)//3][(right_save_current-1)%3]:
                    count2 = count2 + 1
                    right_count2 = count2
                    if right_count2:
                        count2 = count2 - 1
                    
                count2 = count2 + 1
                
            count2 = 0
            for m in range((i-1)//3,len(a)): #아래쪽
                if a[m][(i-1)%3] == a[(left_save_current-1)//3][(left_save_current-1)%3]:
                    left_count2 = count2
                    
                elif a[m][(i-1)%3-1] == a[(left_save_current-1)//3][(left_save_current-1)%3]:
                    count2 = count2 + 1
                    left_count2 = count2
                    if left_count2:
                        count2 = count2 - 1
                    
                if a[m][(i-1)%3] == a[(right_save_current-1)//3][(right_save_current-1)%3]:
                    right_count2 = count2
                    
                elif a[m][(i-1)%3+1] == a[(right_save_current-1)//3][(right_save_current-1)%3]:
                    count2 = count2 + 1
                    right_count2 = count2
                    
                    if right_count2:
                        count2 = count2 - 1
                    
                count2 = count2 + 1

            # print(i, left_count2, right_count2, a[(left_save_current-1)//3][(left_save_current-1)%3], a[(right_save_current-1)//3][(right_save_current-1)%3])

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

    return answer
    
print(solution([0,1,2,3,4,5,6,7,8,0,2,5,8,0], "right"))