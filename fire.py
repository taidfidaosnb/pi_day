def fire(계수리스트, 초기값리스트, limit):
    계수리스트1 = 계수리스트[1:]
    
    def calculation(리스트):
        sum = 0
        for i, j in zip(계수리스트1, 리스트):
            sum += i*j
        return -sum//계수리스트[0]
    count = 1

    for _ in range(len(초기값리스트)):
        yield 초기값리스트[_]
        if count == limit : return
        count += 1

    while count != limit+1:
        yield (calculation(초기값리스트))
        초기값리스트 = 초기값리스트[1:] + [calculation(초기값리스트)]
        count += 1
    return