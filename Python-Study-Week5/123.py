# 알고리즘 설계
# infix 표현식을 각각의 토큰으로 나누어서

# 토큰이 정수라면
# postfix 의 끝에 추가

# 토큰이 연산자라면
# operators 가 빈값이 아닐때까지
# operators 의 마지막 값이 열린 괄호가 아닐때까지
# 토큰의 우선순위 < operators 의 마지막 값의 우선순위일 때까지
# operators 의 마지막 값을 지우고 그것을 postfix 에 추가
# operators 의 끝에 token 추가

# token 이 열린 괄호라면
# operators 의 마지막에 token 추가

# token 이 닫힌 괄호라면
# operators 의 마지막 값이열린 괄호가 아닐때까지
# operators 의 마지막 값을 지우고 그것을 postfix 에 추가
# operators 의 끝에 열리 괄호 추가

# operators 가 빈 배열이 아닐때까지
# operators 의 마지막 값을 지우고 그것을 postfix 에 추가

operators = []
postfix = []


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
    # 모든 공백 제거
    s = expression.replace(" ", "")
    tokens = []
    i = 0
    while i < len(s):
        # *, /, ^, (, ) 와 같은 단일 문자를 다룰 때
        if s[i] in '''*/^()''':
            tokens.append(s[i])
            i += 1
        # +, - 와 같은 단일 문자를 다룰 때
        elif s[i] in '''+-''':
            # i 가 0보다 크고(i-1 인덱스에 접근하기 위해서) s[i-1] 이 0~9, )와 같은 문자일 때
            if i > 0 and (s[i - 1] in '''0123456789)'''):
                tokens.append(s[i])
                i += 1
            # +, - 가 숫자의 일부일(아마 문자열 시작할 때에나 곱셈, 나눗셈 등의 연산에서 양수 혹은 정수를 나타내기 위함)
            else:
                num = s[i]
                i += 1
                # 현재의 i 부터 시작하여 그 다음 정수가 끝이 날때까지 반복문을 돌린 값을 토큰값에 넣어줌 (양수 혹은 음수)
                while i < len(s) and "0" <= s[i] <= "9":
                    num = num + s[i]
                    i = i + 1
                tokens.append(num)
        # 일반적인 숫자일때 아마 부호도 없으며 연산이 되기 전인 맨 처음의 숫자일 때
        elif "0" <= s[i] <= "9":
            num = ""
            # 현재의 i 부터 시작하여 그 다음 정수가 끝이 날때까지 반복문을 돌린 값을 토큰값에 넣어줌 (양수 혹은 음수)
            while i < len(s) and "0" <= s[i] <= "9":
                num = num + s[i]
                i += 1
            tokens.append(num)
        else:
            return []
    return tokens


def infix2postfix(tokens):
    for token in tokens:
        if isInteger(token):
            postfix.append(token)
        elif token == "(":
            operators.append(token)
        elif token == ")":
            while operators[len(operators) -1] != "(":
                postfix.append(operators[len(operators) -1])
                del operators[len(operators) - 1]
            del operators[len(operators) - 1]
        else:
            while len(operators):
                print(1)
                if operators[len(operators) -1] != "(" and precedence(token) < precedence(operators[len(operators) -1]):
                    postfix.append(operators[len(operators) - 1])
                    del operators[len(operators) - 1]
            operators.append(token)
    while len(operators):
        postfix.append(operators[len(operators) - 1])
        del operators[len(operators) - 1]
    return postfix


print(infix2postfix(tokenizing(input('수식이 포함된 문자열을 입력해주세요. '))))