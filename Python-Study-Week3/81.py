# short1 과 short2 를 매개변수로 하는 pita 함수 선언
# 함수 내용은 short1 의 제곱과 shor2 의 제곱을 합한 값의 제곱근을 출력


def pita(short1, short2):
    print(((short1 ** 2) + (short2 ** 2)) ** 0.5)


pita(int(input('첫번째 짧은 변을 입력하세요. ')), int(input('두번째 짧은 변을 입력하세요. ')))