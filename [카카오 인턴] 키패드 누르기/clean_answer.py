#내가 푼게 깔끔
def solution(numbers, hand):

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
        if i == 0:
            i = 11

        if i in (1, 4, 7, '*'):
            answer = answer + 'L'
            left_save_current = i
        elif i in (3, 6, 9, '#'):
            answer = answer + 'R'
            right_save_current = i
        else:
            left_distance = abs(((left_save_current-1)//3)-((i-1)//3)) + abs(((left_save_current-1)%3)-((i-1)%3))
            right_distance = abs(((right_save_current-1)//3)-((i-1)//3)) + abs(((right_save_current-1)%3)-((i-1)%3))
            
            if left_distance < right_distance:
                answer = answer + 'L'
                left_save_current = i
            elif left_distance > right_distance:
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


print(solution([1],"left"))