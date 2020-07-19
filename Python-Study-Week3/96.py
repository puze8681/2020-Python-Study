def checkPassword(password):
    isLength = False
    isUpper = False
    isLower = False
    isNumber = False
    if len(password) > 7:
        isLength = True
    for c in password:
        if c.isupper():
            isUpper = True
        elif c.islower():
            isLower = True
        elif c.isdigit():
            isNumber = True
    if isLength and isUpper and isLower and isNumber:
        print(True)
    else:
        print(False)


checkPassword(input('비밀번호를 입력해주세요. '))
