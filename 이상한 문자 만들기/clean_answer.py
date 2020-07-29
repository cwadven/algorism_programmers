def toWeirdCase(s):
    # 함수를 완성하세요
    return ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split()])

print(toWeirdCase("wow my name is really oogod"))