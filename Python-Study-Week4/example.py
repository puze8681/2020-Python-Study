# 118번
# 모양은 네가지 스페이드 하트 다이아 클럽
# 숫자값은 2~10, K, J, Q, A
# createDeck이라는 함수 생성, 루프를 이용해 모든 카드에 대한 2자 약어 리스트에 저장
# 카드목록을 반환하기(매개변수x)
# 리스트에 있는 카드의 순서 랜덤화하는 shuffle이라는 함수를 쓰시오(각요소 방문,교환)
# shuffle방법 잘모르겠음..
# 셔플하기전과 셔플한 후를 모두 표시
# 랜덤 내장함수 쓰지 x

def createDeck():
    one = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    two = ['s', 'h', 'd', 'c']

    card = [x + y for x in one for y in two]

    return card


card = createDeck()
print('처음 카드목록: ', card)


def shuffle():  # 방법을 모르겠어서 구글링한거..
    n = 52
    start = 0
    while n:  # n=0이 될
        print(n)
        for _ in range(round(n / 2)):  # _는 어떤 특정값을 무시하기 위한 용도로 쓰이기도함
            card.append(card.pop(start))  # pop()은 요소제거
        n = round(n / 2)
        start = start + (n - round(n / 2))
    return card


print('\n한번 셔플한 카드목록 :', shuffle())