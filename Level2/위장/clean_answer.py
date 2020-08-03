import collections
from functools import reduce

# reduce 여러 개의 데이터를 대상으로 주로 누적 집계를 내기 위해서 사용
# reduce(lambda x, y: x*y_함수, 리스트값은값_더할 값들_y파라미터에 들어감, 초기값 및 더해지는 것이 저장되는 장소_x파라미터에들어감)

# Counter --> 리스트 안에 있는 값의 동일한 값이 몇개있는지 dict로 반환
# 반환하는 key 값이 리스트안의 값이고 value 값은 개수이다

def solution(c):
    return reduce(lambda x, y:x*y,[a+1 for a in collections.Counter([x[1] for x in c]).values()],1)-1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))