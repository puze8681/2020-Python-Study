def hex2int(hexNumber):
    result = 0
    for c in hexNumber:
        if c.isalpha():
            result += {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}.get(str(c), 0)
        else:
            result += int(c)
    return result


def int2hex(number):
    return {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}.get(int(number), number)


print(hex2int(input('16진수를 입력해주세요. ')))
print(int2hex(input('10진수를 입력해주세요. ')))
