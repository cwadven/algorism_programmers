def solution(board, moves):  
    # 배열 0으로 초기화
    board2 = list()

    for i in range(len(board)):
        board2.append([])
        for j in range(len(board)):
            board2[i].append(0)

    inside = list()

    answer = 0

    # 수직 수평 위치 변환
    for count2,row in enumerate(board):
        for count, i in enumerate(row):
            board2[count][count2] = i

    # 선택하기
    for i in moves:
        for j in range(len(board2[0])):
            if board2[i-1][j] == 0:
                continue
            else:
                #선택한거 집어 넣기
                if inside[-1:] == [board2[i-1][j]]:
                    inside.pop()
                    answer = answer + 2
                else:
                    inside.append(board2[i-1][j])
                board2[i-1][j] = 0
                break

    return answer

print(solution([
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [1,0,0,0,0,0],
        [1,0,0,0,1,0],
        [1,0,1,0,1,0],
    ], [1,5,3,5,1,2,1,4,1,5,3,5,1,2,1,4]))