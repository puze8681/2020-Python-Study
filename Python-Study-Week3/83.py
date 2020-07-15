# 구매한 품목의 리스트인 number 를 매개변수로 하는 shipping 함수 선언
# 함수 내용은 첫 번째 품목은 10.95달러, 그 이후의 품목은 2.95 달러로 계산하여 전체 배송비를 출력
# number 가 0인 경우 0을 출력
# number 의 수만큼 만복문을 통해 총 값에 2.95 를 더함
# 첫번째 품목의 값은 2.95 보다 8 큰 10.95 로 출력할 때 8을 더해서 출력함


def shipping(number):
    if number == 0:
        print("0")
    else:
        total = 0.0
        for i in range(number):
            total = total + 2.95
        print(total + 8)


shipping(int(input('구매한 품목의 개수를 입력하세요. ')))