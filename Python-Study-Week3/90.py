def isInteger(string):
    string = string.replace(" ", "")
    isNumber = False
    number = 0
    operation = 0
    isBeforeNumber = True
    for c in string:
        if (c == '+' or c == '-') and isBeforeNumber:
            isBeforeNumber = False
            operation += 1
        elif c.isdigit():
            isNumber = True
            isBeforeNumber = True
            number += 1
    if isNumber and len(string) == number + operation:
        print("Integer: True")
    else:
        print("Integer: False")


isInteger(input('문자열을 입력하세요. '))
