def hex2int(hexNumber):
    result = 0
    count = 0
    for c in reversed(hexNumber):
        if c.isalpha():
            result += {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}.get(str(c.upper()), 0) * (16 ** count)
        else:
            result += int(c) * (16 ** count)
        count += 1
    return result


def int2hex(number):
    return {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}.get(int(number), number)


print(hex2int(input('16진수를 입력해주세요. ')))
print(int2hex(input('10진수를 입력해주세요. ')))
