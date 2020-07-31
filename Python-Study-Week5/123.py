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
    return isNumber and len(string) == number + operation


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
    return result


def tokenizing(expression):
    s = expression.replace(" ", "")
    tokens = []
    i = 0
    while i < len(s):
        if s[i] in '''*/^()''':
            tokens.append(s[i])
            i += 1
        elif s[i] in '''+-''':
            if i > 0 and (s[i - 1] in '''0123456789)'''):
                tokens.append(s[i])
                i += 1
            else:
                num = s[i]
                i += 1
                while i < len(s) and "0" <= s[i] <= "9":
                    num = num + s[i]
                    i = i + 1
                tokens.append(num)
        elif "0" <= s[i] <= "9":
            num = ""
            while i < len(s) and "0" <= s[i] <= "9":
                num = num + s[i]
                i += 1
            tokens.append(num)
        else:
            return []
    return tokens


def infix2postfix(tokens):
    operators = []
    postfix = []
    # infix 표현식을 각각의 토큰으로 나누어서
    for token in tokens:
        # 토큰이 정수라면
        if isInteger(token):
            # postfix 의 끝에 추가
            postfix.append(token)

        # token 이 열린 괄호라면
        elif token == "(":
            # operators 의 마지막에 token 추가
            operators.append(token)

        # token 이 닫힌 괄호라면
        elif token == ")":
            # operators 의 마지막 값이열린 괄호가 아닐때까지
            while operators[len(operators) -1] != "(":
                # operators 의 마지막 값을 지우고 그것을 postfix 에 추가
                postfix.append(operators[len(operators) -1])
                del operators[len(operators) - 1]
                # operators 의 끝에 열린 괄호 삭제
            del operators[len(operators) - 1]

        # 토큰이 연산자라면
        else:
            # operators 가 빈값이 아니고
            # operators 의 마지막 값이 열린 괄호가 아니고
            # 토큰의 우선순위 < operators 의 마지막 값의 우선순위일 때까지
            while len(operators) and operators[len(operators) -1] != "(" and precedence(token) < precedence(operators[len(operators) -1]):
                # operators 의 마지막 값을 지우고 그것을 postfix 에 추가
                postfix.append(operators[len(operators) - 1])
                del operators[len(operators) - 1]
            # operators 의 끝에 token 추가
            operators.append(token)

    # operators 가 빈 배열이 아닐때까지
    while len(operators):
        # operators 의 마지막 값을 지우고 그것을 postfix 에 추가
        postfix.append(operators[len(operators) - 1])
        del operators[len(operators) - 1]

    return postfix


print(infix2postfix(tokenizing(input('수식이 포함된 문자열을 입력해주세요. '))))