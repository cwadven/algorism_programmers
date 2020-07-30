def rm_small(mylist):
    #새로운 리스트를 만드는데, 리스트에서 가장 작은 녀석보다 큰 것을 기준으로 리스트를 만든다!
    return [i for i in mylist if i > min(mylist)]