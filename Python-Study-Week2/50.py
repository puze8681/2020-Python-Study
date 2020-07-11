constants = input('a, b, c 를 입력하세요. ').split()
a = int(constants[0])
b = int(constants[1])
c = int(constants[2])
if a == 0:
    print("a 는 0이 아닙니다.")
else:
    discriminant = (b**2) - (4*a*c)
    if discriminant < 0:
        print("실근의 개수는 0개")
    elif discriminant == 0:
        print("실근의 개수 1개")
        print(int((b * -1) / (2*a)))
    else:
        print("실근의 개수는 2개")
        print(int(((b * -1) + discriminant ** 0.5) / (2*a)) ,",", int(((b * -1) - discriminant ** 0.5) / (2*a)))