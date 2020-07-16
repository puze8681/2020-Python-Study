# 세개의 숫자를 매개변수로 하는 median 함수 선언
# 함수 내용은 세개의 숫자 중 중앙값을 출력
# number2 와 number3 중 적은 값과 많으 값을 분별하여 less 와 more 에 대입함
# number1 이 less 보다 작으면 적은 값이 중앙값
# number1 이 more 보다 크면 많은 값이 중앙값
# 그렇지 않으면 number1 이 중앙값이다.


def median(number1, number2, number3):
    less = number2
    more = number3
    if number2 > number3:
        less = number3
        more = number2

    if number1 < less:
        print(less)
    elif more < number1:
        print(more)
    else:
        print(number1)


median(int(input('첫번째 값을 입력하세요. ')), int(input('두번째 값을 입력하세요. ')), int(input('세번째 값을 입력하세요. ')))