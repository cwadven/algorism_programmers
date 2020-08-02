# def solution(priorities, location):
#     answer = list()
#     # 1. 가장 큰 위치 찾기 (index)
#     # 2. 그 전까지의 위치를 위로 땡기기
#     _get = priorities[location]
#     big_index = priorities.index(max(priorities))
#     answer = priorities[big_index:] + priorities[:big_index]
#     if big_index <= location:
#         b=answer.index(_get)+1
#     else:
#         b=answer.index(_get)+len(priorities[big_index:])
#     return b

# print(solution([1, 1, 1, 1, 1, 1],3))

# def solution(priorities, location):
#     before_dict = dict()
#     change_dict = dict()

#     for count, i in enumerate(priorities):
#         before_dict[count]=i

#     # location 위치 찾기
#     big_index = priorities.index(max(priorities))

#     # test dictionary 분리한것 test2에 넣기
#     for key, value in before_dict.items():
#         if key >= big_index:
#             change_dict[key] = value

#     for key, value in before_dict.items():
#         if key < big_index:
#             change_dict[key] = value
    
#     answer_list = list(change_dict.keys())

#     return answer_list.index(location)+1
    
# print(solution([1, 2, 3, 4],2))

# 위에는 테스트 케이스가 별로 없어 문제 이해를 잘 못해서 저지른 ㅠㅠ
def solution(priorities, location):
    a = priorities.copy()
    priorities = list(enumerate(priorities))
    count = 0
    while priorities:
        if priorities[0][1] == max(a):
            count = count + 1
            if location == priorities[0][0]:
                break
            priorities = priorities[1:] + priorities[0:1]
            a = a[1:] + a[0:1]
            priorities.pop()
            a.pop()
        else:
            priorities = priorities[1:] + priorities[0:1]
            a = a[1:] + a[0:1]

    return count
    
print(solution([1, 2, 3, 4],2))