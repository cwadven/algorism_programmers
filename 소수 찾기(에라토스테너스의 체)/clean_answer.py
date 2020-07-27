def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            print(set(range(2*i,n+1,i)))
            num-=set(range(2*i,n+1,i))

    return len(num)

#-=을 이용하기 위해서 set를 사용한 것 같음!
#range(2*i,n+1,i)를 한 이유는 2*i을 해야 소수인 2라던지 3이라던지 5라던지 사라지지 않아서

#에라토스테너스의 체