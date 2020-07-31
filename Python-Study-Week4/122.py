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
    print("The tokens are: {}".format(tokens))


tokenizing(input('수식이 포함된 문자열을 입력해주세요. '))
