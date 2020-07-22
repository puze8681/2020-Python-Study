def precedence(string):
    result = -1
    for i in string:
        if i == '+' or i == '-':
            result = 1
    for i in string:
        if i == '*' or i == '/':
            result = 2
    for i in string:
        if i == '^':
            result = 3
    print(result)


precedence(input('문자열을 입력하세요. '))
