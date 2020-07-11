a, b, c = input('숫자 3 개를 입력하세요. ').split()
a = int(a)
b = int(b)
c = int(c)
max = a
if max < b:
    max = b
if max < c:
    max = c
if max > a+b+c - max:
    print("삼각형이 아닙니다.")
else:
    if a == b and b == c and a == c:
        print("정삼각형입니다.")
    elif (a == b and b != c) or (b == c and c != a) or (c == a and a != b):
        print("이등변 삼각형입니다.")
    else:
        print("스칼린입니다.")


