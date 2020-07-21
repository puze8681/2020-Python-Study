def setBase():
    print('이전 베이스는 {}진수 였습니다.'.format(beforeBase))
    return int(input('기본 베이스를 입력해주세요. '))


def convert10(beforeBase, num):
    print("{}진수 {}을 ".format(beforeBase, num), end="")
    if 2 <= beforeBase <= 10:
        num = int(num)
        result = 0
        count = 0
        while 1:
            result += int(num % 10) * (beforeBase ** count)
            count += 1
            if num // 10 == 0:
                break
            else:
                num = num // 10
        return result
    elif 11 <= beforeBase <= 16:
        result = 0
        count = 0
        for c in reversed(num):
            if c.isalpha():
                result += {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}.get(str(c.upper()), 0) * (16 ** count)
            else:
                result += int(c) * (beforeBase ** count)
            count += 1
        return result
    else:
        return -1


def convertBaseNum(afterBase, num10):
    q = int(num10)
    result = list("")
    while 1:
        r = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}.get(q % afterBase, q % afterBase)
        result.insert(0, str(r))
        q = q // afterBase
        if q == 0:
            break
    print("{}진수로 변환한 결과는 {}\n".format(afterBase,''.join(result)))
    return afterBase


beforeBase = 10
while 1:
    afterBase = setBase()
    if 2 <= afterBase <= 16:
        beforeBase = convertBaseNum(afterBase, convert10(beforeBase, input('변환할 숫자를 입력해주세요. ')))
    else:
        break