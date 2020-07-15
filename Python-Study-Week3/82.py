# distance 를 매개변수로 하는 taxi 함수 선언
# 함수 내용은 기본 요금과 추가 요금을 더한 총 요금을 출력
# 추가 요금은 km 단위로 입력받은 거리를 140m 로 나누어진 값과 추가 택시 요금과의 곱
# 기본 요금과 추가 택시 요금은 프로그램을 쉽게 업데이트할 수 있게 상수(baseFare, overFare) 로 선언


def taxi(distance):
    baseFare = 4
    overFare = 0.25
    overTraveled = int((distance * 1000) / 140)
    print(baseFare + overFare * overTraveled)


taxi(int(input('주행 거리를 입력하세요. (단위는 km) ')))