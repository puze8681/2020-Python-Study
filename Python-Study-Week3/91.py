def precedence(string):
    result = -1
    for i in string:
        if i == '+' or i == '-':
            result = 1
        elif i == '*' or i == '/':
            result = 2
        elif i == '^':
            result = 3
    print(result)


precedence(input('문자열을 입력하세요. '))
