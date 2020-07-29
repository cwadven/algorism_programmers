def solution(s):
    s = s.split(" ")
    new = list()
    for number, value in enumerate(s):
        for count, j in enumerate(value):
            if count%2==0:
                new.append(j.upper())
            else:
                new.append(j.lower())
        if len(s)-1 != number:
            new.append(" ")
    # a = [j.upper() for number, value in enumerate(s) for count, j in enumerate(value) if count % 2 == 0]
    return "".join(new)

print(solution("  wow my name is really oogod "))