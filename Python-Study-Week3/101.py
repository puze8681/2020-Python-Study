def fraction(numerator, denominator):
    d = numerator
    if numerator > denominator:
        d = denominator
    while 1:
        if numerator % d == 0 and denominator % d == 0:
            break
        else:
            d -= 1
    print("분자: {}, 분모: {}".format(int(numerator/d), int(denominator/d)))


fraction(int(input('분자를 입력하세요. ')), int(input('분모를 입력하세요. ')))