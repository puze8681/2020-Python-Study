# 빨대 3개의 길이를 매개변수로 하는 triangle 함수 선언
# 함수 내용은 매개변수로 받은 숫자들이 삼각형을 이룰 수 있는지 없는지 Bool 값을 출력
# 가장 긴 빨대의 길이를 찾기 위해 초기값을 빨대 1로 대입
# max 가 빨대 2의 값보다 작다면 max 에 빨대 2를 대입
# max 가 빨대 3의 값보다 작다면 max 에 빨대 3을 대입
# max 값이 빨대 3개의 합에서 max 의 값을 뺀 것 (가장 길지 않은 빨대 2개의 값의 합) 보다 작다면 True 를 출력, 아니라면 False 를 출력
# 1부터 12까지의 경우에 해당하는 결과값을 출력, 범위에 대한 예외에는 해당하는 문자열을 출력
# 만약 1절이 아니라면 후속절을 출력
# 반복문을 통해 song 함수를 12번 호출


def triangle(straw1, straw2, straw3):
    max = straw1
    if max < straw2:
        max = straw2
    if max < straw3:
        max = straw3

    if max < straw1 + straw2 + straw3 - max:
        print(True)
    else:
        print(False)


triangle(int(input('빨대1 의 길이를 입력해주세요. ')), int(input('빨대2 의 길이를 입력해주세요. ')), int(input('빨대3 의 길이를 입력해주세요. ')))
