def solution(bridge_length, weight, truck_weights):
    during = []
    answer = 0

    while truck_weights or during:
        #각각 시간을 가지고 있다!
        try:
            if weight >= sum([i[1] for i in during])+truck_weights[0]:
                during.append([0, truck_weights.pop(0)])
                answer = answer + 1
                for j in during:
                    j[0] = j[0] + 1
                if during[0][0] == bridge_length:
                    during.pop(0)
            else:
                answer = answer + 1
                for j in during:
                    j[0] = j[0] + 1
                if during[0][0] == bridge_length:
                    during.pop(0)
        except:
            answer = answer + 1
            for j in during:
                j[0] = j[0] + 1
            if during[0][0] == bridge_length:
                during.pop(0)
    
    return answer + 1

print(solution(2, 10, [7,4,5,6]))